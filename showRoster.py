import requests
from bs4 import BeautifulSoup
import json
from prettytable import PrettyTable

#Atlanta Reign
#Boston Uprising
#Chengou Hunters
#Dallas Fuel
#Florida Mayhem
#Guangzhou Charge
#Hangzhou Spark
#Houston OutLaws
#London Spitfire
#Los Angeles Gladiators
#Los Angeles Valiant
#New York Excelsior
#Paris Eternal
#Philadelphia Fusion
#San Francicso Shock
#Seoul Dynasty
#Shanghai Dragons
#Toronto Defiant
#Vancouver Titans
#Washington Justice

def showRoster(roster):
  rosterTable = PrettyTable(["Player","Battle Tag","Role","Full Name","Player Number"])
  person = 1
  for player in roster:
    rosterTable.add_row([person,player['name'],player['role'],player['fullName'],player['playerNumber']])
    person += 1
    
  return rosterTable

def getRoster(name):
  html = requests.get("https://"+name+".overwatchleague.com/en-us/roster").text
  soup = BeautifulSoup(html, 'html.parser')
  roster = soup.find("script", {"id":"__NEXT_DATA__"})
  data = json.loads(list(roster)[0])
  return str(showRoster(data['props']['pageProps']['blocks'][2]['roster']['players']))

