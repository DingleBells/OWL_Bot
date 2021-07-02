import discord
import os
from keep_alive import keep_alive
from schedule import*
from getRoster import *
from helpfunction import*;
from getStandings import *;

client = discord.Client()

@client.event
async def on_ready():
  print('We have loggied in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if(msg.startswith("-")):
    
    if(msg.startswith("-roster")): 
      team = (msg.split("-roster ")[1]).lower()
      await message.channel.send(findTeam(team))
    
    elif msg.startswith("-owl standings"):
      response = message.content.split()[2]
      west, east, tourney = owlSchedule(response)
      print(len(west), len(east))
      await message.channel.send(tourney)
      await message.channel.send(west)
      await message.channel.send(east)

    elif msg.startswith("-help"):
      await message.channel.send(embed = getHelp())

    elif (msg.startswith("-owl schedule")):
      await message.channel.send(embed=embedSchedule())

keep_alive()
my_secret = os.environ['token']
client.run(my_secret)