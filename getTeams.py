import datetime
import discord

def getTeams(reign, uprising, hunters, fuel, mayhem, gladiators, charge, outlaws, spark,
spitfire, excelsior, eternal, fusion, dynasty, shock, dragons, defiant, valiant, titans,
justice) :
    teamList = discord.Embed(
        title="Overwatch League Teams",
        description="2021 Season\n"+
        "**"+reign+"ATL-Atlanta Reign**\n"+
        "**"+uprising+"BOS-Boston Uprising**\n"+
        "**"+hunters+"CDH-Chengdu Hunters**\n"+
        "**"+fuel+"DAL-Dallas Fuel**\n"+
        "**"+mayhem+"FLA-Florida Mayhem**\n"+
        "**"+gladiators+"GLA-Los Angeles Gladiators**\n"+
        "**"+charge+"GZC-Guangzhou Charge**\n"+
        "**"+outlaws+"HOU-Houston Outlaws**\n"+
        "**"+spark+"HZS-Hangzhou Spark**\n"+
        "**"+spitfire+"LDN-London Spitfire**\n"+
        "**"+excelsior+"NYE-New York Excelsior**\n"+
        "**"+eternal+"PAR-Paris Eternal**\n"+
        "**"+fusion+"PHI-Philadelphia Fustion**\n"+
        "**"+dynasty+"SEO-Seoul Dynasty**\n"+
        "**"+shock+"SFS-San Francisco Shock**\n"+
        "**"+dragons+"SHD-Shanghai Dragons**\n"+
        "**"+defiant+"TOR-Toronto Defiant**\n"
        "**"+valiant+"VAL-Los Angeles Valiant**\n"+
        "**"+titans+"VAN-Vancouver Titans**\n"+
        "**"+justice+"WAS-Washington Justice**",
        color=discord.Colour.gold(),
        timestamp=datetime.datetime.utcnow()
    )
    return teamList
