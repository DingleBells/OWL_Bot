import datetime
import requests
import discord
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
import json

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def formatDate(month, day, hour, minute):
    if minute == 0:
        minute = "00"
    elif minute <=10:
        minute = f"0{minute}"
    if hour >= 12:
        if hour != 12:
            hour %= 12
        thing = "PM"
    else:
        thing = "AM"
    return f"{month}/{day} @ {hour}:{minute} {thing}"


def getWeekSchedule():
    pagehtml = requests.get("https://overwatchleague.com/en-us/schedule").text
    soup = BeautifulSoup(pagehtml, 'html.parser')
    things = soup.find("script", {"id": "__NEXT_DATA__"})
    data = json.loads(list(things)[0])
    weekschedule = []
    for match in data['props']['pageProps']['blocks'][2]['schedule']['tableData']['events'][0]['matches']:
        competitors = (match['competitors'][0]['name'], match['competitors'][1]['name'])
        matchtime = time.localtime(match['startDate'] / 1000)
        if match['isEncore'] == True:
            c1, c2 = competitors
            c2 += " (Encore)"
            matchtime = time.localtime(match['encoreDate'] / 1000)
            competitors = (c1, c2)
        weekschedule.append(
            (competitors, formatDate(matchtime.tm_mon, matchtime.tm_mday, matchtime.tm_hour, matchtime.tm_min)
             , match['status'] == "CONCLUDED"))
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
    return commands