import datetime
import requests
from bs4 import BeautifulSoup
import json
import discord

def formatName(name):
    nameDict = {
                "reign":"Atlanta", 'uprising':"Boston", 'hunters':"Chengdu",
                "fuel":"Dallas", "mayhem":"Florida", 'charge':"Guangzhou",
                "spark":"Hangzhou", 'outlaws':"Houston", "spitfire":"London",
                "gladiators":"Los Angeles", "valiant":"Los Angeles", "eternal":"Paris",
                "fusion":"Philadelphia", "shock":"San Francisco", "dynasty":"Seoul",
                "dragons":"Shanghai", "defiant":"Toronto", "titans":"Vancouver", "justice":"Washington"
                }
    return nameDict[name] + " " + name

def getRosterEmbed(teamname):
    name = teamname.split()[-1]
    html = requests.get("https://" + name + ".overwatchleague.com/en-us/roster").text
    soup = BeautifulSoup(html, 'html.parser')
    roster = soup.find("script", {"id": "__NEXT_DATA__"})
    players = json.loads(list(roster)[0])['props']['pageProps']['blocks'][2]['roster']['players']
    #https://stackoverflow.com/questions/54937474/discord-bot-embed-custom-emojiawait message.channel.send(embed=embedname)
    tanks = 0
    dps = 0
    supports = 0
    data = []

    namestuff = ""
    rolestring = ""

    for player in players:
        if player['role'] == "Tank":
            tanks += 1
            rolestring += "<:tank:864277276086108160>\n"
        elif player['role'] == "Offense":
            dps += 1
            rolestring += "<:dps:864277301364260905>\n"
        else:
            supports += 1
            rolestring += "<:support:864277141068054568>\n"
        fullname = player['fullName'].split()
        namestuff += fullname[0] + "** " + player['name'] + " **" + " ".join(fullname[1:]) + "\n"
        data.append((player['name'], player['role'], player['fullName']))

    embed = discord.Embed(
        title=f"{formatName(name).title()} Roster",
        description=f"{tanks} Tanks, {dps} DPS, {supports} Supports",
        timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(name="Role", value=rolestring)
    embed.add_field(name='Player', value=namestuff)
    return embed
