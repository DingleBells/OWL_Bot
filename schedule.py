import requests
import discord
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time
import json


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
    pagehtml = requests.get("https://overwatchleague.com/en-us/schedule?stage=regular_season&week=12").text
    soup = BeautifulSoup(pagehtml, 'html.parser')
    things = soup.find("script", {"id": "__NEXT_DATA__"})
    data = json.loads(list(things)[0])

    weekschedule = []

    for match in data['props']['pageProps']['blocks'][2]['schedule']['tableData']['events'][0]['matches']:
        competitors = (match['competitors'][0]['name'], match['competitors'][1]['name'])
        matchtime = time.gmtime(match['startDate'] / 1000)
        # print(matchtime)
        # print(competitors, matchtime.tm_mon, matchtime.tm_mday, matchtime.tm_hour - 7, matchtime.tm_min)
        weekschedule.append((competitors, formatDate(matchtime.tm_mon, matchtime.tm_mday, matchtime.tm_hour - 7, matchtime.tm_min)))
    return weekschedule

def formatSchedule(schedule):
    table = PrettyTable(["Time", "Matchup"])
    for ((team1, team2), mytime) in schedule:
        # print(team1, team2, mytime)
        table.add_row([mytime, f"{team1} vs. {team2}"])
    return table


def embedSchedule():
    commands = discord.Embed(
        title="OWL Schedule",
        description="The Overwatch League's Schedule for this Week!",
        color=discord.Colour.gold()
    )

    games = getWeekSchedule()
    for ((team1, team2), mytime) in games:
        commands.add_field(name=mytime, value=f"{team1} vs. {team2}")
    return commands