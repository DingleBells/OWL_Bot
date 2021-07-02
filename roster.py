import requests
from bs4 import BeautifulSoup
import json
from prettytable import PrettyTable

#Atlanta Reign
ARhtml = requests.get("https://reign.overwatchleague.com/en-us/roster").text
ARsoup = BeautifulSoup(ARhtml, 'html.parser')
ARroster = ARsoup.find("script", {"id":"__NEXT_DATA__"})
ARdata = json.loads(list(ARroster)[0])
#Boston Uprising
BUhtml = requests.get("https://uprising.overwatchleague.com/en-us/roster").text
BUsoup = BeautifulSoup(BUhtml, 'html.parser')
BUroster = BUsoup.find("script", {"id":"__NEXT_DATA__"})
BUdata = json.loads(list(BUroster)[0])
#Chengou Hunters
CHhtml = requests.get("https://hunters.overwatchleague.cn/en-us/roster").text
CHsoup = BeautifulSoup(CHhtml, 'html.parser')
CHroster = CHsoup.find("script", {"id":"__NEXT_DATA__"})
CHdata = json.loads(list(CHroster)[0])
#Dallas Fuel
DFhtml = requests.get("https://fuel.overwatchleague.com/en-us/roster").text
DFsoup = BeautifulSoup(DFhtml, 'html.parser')
DFroster = DFsoup.find("script", {"id":"__NEXT_DATA__"})
DFdata = json.loads(list(DFroster)[0])
#Florida Mayhem
FMhtml = requests.get("https://mayhem.overwatchleague.com/en-us/roster").text
FMsoup = BeautifulSoup(FMhtml, 'html.parser')
FMroster = FMsoup.find("script", {"id":"__NEXT_DATA__"})
FMdata = json.loads(list(FMroster)[0])
#Guangzhou Charge
GChtml = requests.get("https://charge.overwatchleague.cn/en-us/roster").text
GCsoup = BeautifulSoup(GChtml, 'html.parser')
GCroster = GCsoup.find("script", {"id":"__NEXT_DATA__"})
GCdata = json.loads(list(GCroster)[0])
#Hangzhou Spark
HShtml = requests.get("https://spark.overwatchleague.cn/en-us/roster").text
HSsoup = BeautifulSoup(HShtml, 'html.parser')
HSroster = HSsoup.find("script", {"id":"__NEXT_DATA__"})
HSdata = json.loads(list(HSroster)[0])
#Houston OutLaws
HOhtml = requests.get("https://outlaws.overwatchleague.com/en-us/roster").text
HOsoup = BeautifulSoup(HOhtml, 'html.parser')
HOroster = HOsoup.find("script", {"id":"__NEXT_DATA__"})
HOdata = json.loads(list(HOroster)[0])
#London Spitfire
LShtml = requests.get("https://spitfire.overwatchleague.com/en-us/roster").text
LSsoup = BeautifulSoup(LShtml, 'html.parser')
LSroster = LSsoup.find("script", {"id":"__NEXT_DATA__"})
LSdata = json.loads(list(LSroster)[0])
#Los Angeles Gladiators
LAGhtml = requests.get("https://gladiators.overwatchleague.com/en-us/roster").text
LAGsoup = BeautifulSoup(LAGhtml, 'html.parser')
LAGroster = LAGsoup.find("script", {"id":"__NEXT_DATA__"})
LAGdata = json.loads(list(LAGroster)[0])
#Los Angeles Valiant
LAVhtml = requests.get("https://valiant.overwatchleague.com/en-us/roster").text
LAVsoup = BeautifulSoup(LAVhtml, 'html.parser')
LAVroster = LAVsoup.find("script", {"id":"__NEXT_DATA__"})
LAVdata = json.loads(list(LAVroster)[0])
#New York Excelsior
NYEhtml = requests.get("https://excelsior.overwatchleague.com/en-us/roster").text
NYEsoup = BeautifulSoup(NYEhtml, 'html.parser')
NYEroster = NYEsoup.find("script", {"id":"__NEXT_DATA__"})
NYEdata = json.loads(list(NYEroster)[0])
#Paris Eternal
PEhtml = requests.get("https://eternal.overwatchleague.com/en-us/roster").text
PEsoup = BeautifulSoup(PEhtml, 'html.parser')
PEroster = PEsoup.find("script", {"id":"__NEXT_DATA__"})
PEdata = json.loads(list(PEroster)[0])
#Philadelphia Fusion
PFhtml = requests.get("https://fusion.overwatchleague.com/en-us/roster").text
PFsoup = BeautifulSoup(PFhtml, 'html.parser')
PFroster = PFsoup.find("script", {"id":"__NEXT_DATA__"})
PFdata = json.loads(list(PFroster)[0])
#San Francicso Shock
SFShtml = requests.get("https://shock.overwatchleague.com/en-us/roster").text
SFSsoup = BeautifulSoup(SFShtml, 'html.parser')
SFSroster = SFSsoup.find("script", {"id":"__NEXT_DATA__"})
SFSdata = json.loads(list(SFSroster)[0])
#Seoul Dynasty
SEDhtml = requests.get("https://dynasty.overwatchleague.com/en-us/roster").text
SEDsoup = BeautifulSoup(SEDhtml, 'html.parser')
SEDroster = SEDsoup.find("script", {"id":"__NEXT_DATA__"})
SEDdata = json.loads(list(SEDroster)[0])
#Shanghai Dragons
SDhtml = requests.get("https://dragons.overwatchleague.cn/en-us/roster").text
SDsoup = BeautifulSoup(SDhtml, 'html.parser')
SDroster = SDsoup.find("script", {"id":"__NEXT_DATA__"})
SDdata = json.loads(list(SDroster)[0])
#Toronto Defiant
TDhtml = requests.get("https://defiant.overwatchleague.com/en-us/roster").text
TDsoup = BeautifulSoup(TDhtml, 'html.parser')
TDroster = TDsoup.find("script", {"id":"__NEXT_DATA__"})
TDdata = json.loads(list(TDroster)[0])
#Vancouver Titans
VThtml = requests.get("https://titans.overwatchleague.com/en-us/roster").text
VTsoup = BeautifulSoup(VThtml, 'html.parser')
VTroster = VTsoup.find("script", {"id":"__NEXT_DATA__"})
VTdata = json.loads(list(VTroster)[0])
#Washington Justice
WJhtml = requests.get("https://justice.overwatchleague.com/en-us/roster").text
WJsoup = BeautifulSoup(WJhtml, 'html.parser')
WJroster = WJsoup.find("script", {"id":"__NEXT_DATA__"})
WJdata = json.loads(list(WJroster)[0])


def showRoster(roster):
  rosterTable = PrettyTable(["Player","Battle Tag","Role","Full Name","Player Number"])
  person = 1
  for player in roster:
    rosterTable.add_row([person,player['name'],player['role'],player['fullName'],player['playerNumber']])
    person += 1
    
  return rosterTable

def getAtlantaRoster():
  return str(showRoster(ARdata['props']['pageProps']['blocks'][2]['roster']['players']))

def getBostonRoster():
  return "```"+str(showRoster(BUdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getChengouRoster():
  return "```"+str(showRoster(CHdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getDallasRoster():
  return "```"+str(showRoster(DFdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getFloridaRoster():
  return "```"+str(showRoster(FMdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getGuangzhouRoster():
  return "```"+str(showRoster(GCdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getHangzhouRoster():
  return "```"+str(showRoster(HSdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getHoustonRoster():
  return "```"+str(showRoster(HOdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getLondonRoster():
  return "```"+str(showRoster(LSdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getLAGRoster():
  return "```"+str(showRoster(LAGdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getLAVRoster():
  return "```"+str(showRoster(LAVdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getNYRoster():
  return "```"+str(showRoster(NYEdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getParisRoster():
  return "```"+str(showRoster(PEdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getPhiladelphiaRoster():
  return "```"+str(showRoster(PFdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getSFSRoster():
  return "```"+str(showRoster(SFSdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getSeoulRoster():
  return "```"+str(showRoster(SEDdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getShanghaiRoster():
  return "```"+str(showRoster(SDdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getTorontoRoster():
  return "```"+str(showRoster(TDdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getVancouverRoster():
  return "```"+str(showRoster(VTdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"

def getWashingtonRoster():
  return "```"+str(showRoster(WJdata['props']['pageProps']['blocks'][2]['roster']['players']))+"```"