from urllib.request import urlopen as uReq
import discord
from bs4 import BeautifulSoup as soup
from prettytable import PrettyTable
import json


def displayStandings(stuff):
    westTable = PrettyTable([f"Rank", "Team", "Pts", "W", "L", "Map W-L-T", "Diff"])
    tables = stuff['tables']
    west = tables[0]
    teams = west['teams']
    rank = 1
    filler = '-'
    for team in teams:
        # print(team)
        if team['type'] == 'team':
            westTable.add_row([rank, team['teamAbbName'], team['pts'], team['w'], team['l'],
                               team['mapwlt'], team['diff']])
        else:
            westTable.add_row([filler, filler, filler, filler, filler, filler, filler])
        rank += 1
    eastTable = PrettyTable([f"Rank", "Team", "Pts", "W", "L", "Map W-L-T", "Diff"])
    east = tables[1]
    teams = east['teams']
    rank = 1
    for team in teams:
        if team['type'] == 'team':
            eastTable.add_row([rank, team['teamAbbName'], team['pts'], team['w'], team['l'],
                               team['mapwlt'], team['diff']])
        else:
            eastTable.add_row([filler, filler, filler, filler, filler, filler, filler])
        rank += 1
    return westTable, eastTable


def getStandings(tourney):
    # tourney: 0 = reg season, 1 = may melee, 2 = june joust, 3 = summer showdown, 4 = countdown cup
    tourneyDict = {0: '2021 Regular Season', 1: "May Melee Qualifiers", 2: 'June Joust: Qualifiers'
        , 3: 'Summer Showdown: Qualifiers', 4: 'Countdown Cup: Qualifiers'}
    # get the raw html data
    my_url = 'https://overwatchleague.com/en-us/standings/2021/summer-showdown-qualifiers'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # find the data that we need and convert it into a dictionary
    page_soup = soup(page_html, "html.parser")
    things = page_soup.find("script", {"id": "__NEXT_DATA__"})
    data = json.loads(list(things)[0])
    standings = data['props']['pageProps']['blocks'][1]['standings']['tabs']

    # return the data
    for i in range(5):
        if standings[i]['title'] == tourneyDict[tourney]:
            west, east = displayStandings(standings[i])
            return west, east


def makeStandingsEmbed(west, east, title):
    standings = discord.Embed(
        title=title + " Standings"
    )
    standings.add_field(name='West Region Standings', value="```" + str(west) + "```", inline=True)
    standings.add_field(name='East Region Standings', value='```' + str(east) + "```", inline=False)
    return standings


def getStandingsEmbed(tourney):
    # tourney: 0 = reg season, 1 = may melee, 2 = june joust, 3 = summer showdown, 4 = countdown cup
    tourneyDict = {0: '2021 Regular Season', 1: "May Melee Qualifiers", 2: 'June Joust: Qualifiers'
        , 3: 'Summer Showdown: Qualifiers', 4: 'Countdown Cup: Qualifiers'}
    # get the raw html data
    my_url = 'https://overwatchleague.com/en-us/standings/2021/summer-showdown-qualifiers'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # find the data that we need and convert it into a dictionary
    page_soup = soup(page_html, "html.parser")
    things = page_soup.find("script", {"id": "__NEXT_DATA__"})
    data = json.loads(list(things)[0])
    standings = data['props']['pageProps']['blocks'][1]['standings']['tabs']

    # return the data
    for i in range(5):
        if standings[i]['title'] == tourneyDict[tourney]:
            west, east = displayStandings(standings[i])
    return makeStandingsEmbed(west, east, tourneyDict[tourney])
