import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import discord

def getSchedule(week):
    options = Options()
    options.headless = True

    driver = webdriver.Chrome('/home/kanghee/bin/chromedriver', options=options)
    driver.get(f'https://overwatchleague.com/en-us/schedule?stage=regular_season&week={week}')

    print('driver.get is completed')
    schedules = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[3]")
    fout = open("HTMLInHere.txt", 'w')
    fout.write(schedules.text)

    schedulelist = schedules.text.split("\n")

    matchlist = [schedulelist[20].title()]
    start = 25

    for i in range(25, len(schedulelist)):
        try:
            date = int(schedulelist[i].split()[2])
            matchlist.append(tuple(schedulelist[start:i]))
            start = i
        except:
            continue
    matchlist.append(schedulelist[start:])
    driver.quit()
    return matchlist


def handleMatchDates(response):
    inlist = getSchedule(response)
    embed = discord.Embed(
        title="Overwatch League" + inlist[0] + " Schedule",
        color=discord.Colour.gold(),
        timestamp=datetime.datetime.utcnow()
    )
    outlist = []
    for match in inlist:
        if "-" in match: # in progress/completed
            embed.add_field(name=match[0].title(), value=f"{match[2]} ||{match[3]}-{match[5]}|| {match[6]}")
        elif "@" in match:
            embed.add_field(name=match[0].title() + " @ " + match[1], value=f"{match[2]} vs. {match[4]}")
    return embed
