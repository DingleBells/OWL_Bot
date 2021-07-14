import datetime
import requests
from bs4 import BeautifulSoup
import discord
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

def getScores():
    pagehtml = requests.get("https://overwatchleague.com/en-us/schedule").text
    soup = BeautifulSoup(pagehtml, 'html.parser')
    things = soup.find("script", {"id": "__NEXT_DATA__"})
    data = json.loads(list(things)[0])

    concludedMatches = []

    for match in data['props']['pageProps']['blocks'][2]['schedule']['tableData']['events'][0]['matches']:
        if match['status'] in ['CONCLUDED', "IN_PROGRESS"] and not match['isEncore']:

            matchtime = time.gmtime(match['startDate'] / 1000)

            team1, team2 = match['competitors'][0]['abbreviatedName'], match['competitors'][1]['abbreviatedName']
            score = match['scores']
            concludedMatches.append((team1, team2, score,
                        formatDate(matchtime.tm_mon, matchtime.tm_mday, matchtime.tm_hour - 7, matchtime.tm_min ),
                                     match['link']))
        else:
            break

    return concludedMatches


def getScoreEmbed():
    embed = discord.Embed(
        title="Overwatch League Scores from this Week",
        description="Completed/In Progress Overwatch League Matches!\n For more details, click on the score.",
        color=discord.Colour.gold(),
        timestamp=datetime.datetime.utcnow()
    )
    data = getScores()
    counter = 0
    for (m1, m2, [s1, s2], date, link) in data:
        counter += 1
        embed.add_field(name=date,value=f"[{m1} {s1} - {s2} {m2}]({link})", inline=True)
    if counter % 3 == 2:
      embed.add_field(name='\u200b', value='\u200b')
    return embed

