import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have loggied in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

keep_alive()
my_secret = os.environ['token']
client.run(my_secret)