import discord
import os
import requests
from bs4 import BeautifulSoup
import json
from keep_alive import keep_alive

pagehtml = requests.get("https://shock.overwatchleague.com/en-us/roster").text
soup = BeautifulSoup(pagehtml, 'html.parser')
things = soup.find("script", {"id": "__NEXT_DATA__"})
print(things)
data = json.loads(list(things)[0])


client = discord.Client()

@client.event
async def on_ready():
  print('We have loggied in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if(message.content.startswith("-")):
    if(message.content.startswith("-hello")):
      await message.channel.send('Hello!')
    
    if(message.content.startswith('-roster shock')):
      await message.channel.send('SF shock roster')

keep_alive()
my_secret = os.environ['token']
client.run(my_secret)