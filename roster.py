import requests
from bs4 import BeautifulSoup
import json
from prettytable import PrettyTable

pagehtml = requests.get("https://shock.overwatchleague.com/en-us/roster").text
soup = BeautifulSoup(pagehtml, 'html.parser')
things = soup.find("script", {"id": "__NEXT_DATA__"})
data = json.loads(list(things)[0])


def showRoster(roster):
  rosterTable = PrettyTable(["Player","Battle Tag","Role","Full Name","Player Num"])
  person = 1
  for player in roster:
    rosterTable.add_row([person,player['name'],player['role'],player['fullName'],player['playerNumber']])
    person += 1
    
  
  return rosterTable


def getShockRoster(name):
  return "```"+str(showRoster(data['props']['pageProps']['blocks'][2]['roster']['players']))+"```"
  
