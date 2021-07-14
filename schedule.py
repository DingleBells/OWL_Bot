import datetime
import requests
import discord
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
import json

def convertUTCToPST(intime):
    # pst is 7 hours behind UTC
    intime = intime.split()

    monthdate = intime[0].split('-')
    month = int(monthdate[1])
    date = int(monthdate[2])

    hourmin = intime[1].split(':')
    hour = int(hourmin[0])
    min = int(hourmin[1])

    if hour >= 7:
        hour -= 7
    else:
        hour = 24 + hour-7
        if date == 1:
            if month == 1:
                month = 12
            else:
                month -= 1
            if month in [1, 3, 5, 7, 8, 10, 12]:
                date = 31
            elif month == 2:
                date = 28
            else:
                date = 30
        else:
            date -= 1

    if min == 0:
        min = "00"
    elif min <= 10:
        min = f"0{min}"
    if hour >= 12:
        if hour != 12:
            hour %= 12
        thing = "PM"
    else:
        thing = "AM"
    return f"{month}/{date} @ {hour}:{min} {thing}"

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def getWeekSchedule():
    pagehtml = requests.get("https://overwatchleague.com/en-us/schedule").text
    soup = BeautifulSoup(pagehtml, 'html.parser')
    things = soup.find("script", {"id": "__NEXT_DATA__"})
    data = json.loads(list(things)[0])
    weekschedule = []
    for match in data['props']['pageProps']['blocks'][2]['schedule']['tableData']['events'][0]['matches']:
        competitors = (match['competitors'][0]['name'], match['competitors'][1]['name'])
        matchtime = datetime.datetime.utcfromtimestamp(match['startDate'] / 1000)
        if match['isEncore'] == True:
            c1, c2 = competitors
            c2 += " (Encore)"
            matchtime = datetime.datetime.utcfromtimestamp(match['encoreDate'] / 1000)
            competitors = (c1, c2)
        weekschedule.append((competitors, convertUTCToPST(str(matchtime)), match['status'] == "CONCLUDED"))
    return weekschedule


def embedSchedule():
    commands = discord.Embed(
        title="OWL Schedule",
        description="The Overwatch League's Schedule for this Week!",
        color=discord.Colour.gold(),
        timestamp=datetime.datetime.utcnow()
    )

    games = getWeekSchedule()
    for ((team1, team2), mytime, strikethrough) in games:
        if strikethrough:
            commands.add_field(name=f"~~{mytime}~~", value=f"~~{team1} vs. {team2}~~")
        else:
            commands.add_field(name=mytime, value=f"{team1} vs. {team2}")
    commands.set_footer(text='Note: All times are in PST')
    return commands