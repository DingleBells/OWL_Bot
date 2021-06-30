import discord
import os
import requests
from bs4 import BeautifulSoup
import json
from prettytable import PrettyTable
from keep_alive import keep_alive
from schedule import*
from roster import*
from replit import db

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
    
    elif(message.content.startswith('-roster shock')):
      await message.channel.send(getShockRoster("shock"))
    
    elif (message.content.startswith("-owl schedule")):
      await message.channel.send(embed=embedSchedule())

keep_alive()
my_secret = os.environ['token']
client.run(my_secret)