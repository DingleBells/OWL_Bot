import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']+" -"+json_data[0]['a']
  return quote

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    db["encouragements"].append(encouraging_message)
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  print(encouragements)
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

sad_words = ["sad","depressed","unhappy","angry","miserable"]

@client.event
async def on_ready():
  print('We have loggied in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  encouragements = ["Cheer up!","You got this!","You can do this!","Never give up!","Hang in there!"]
  
  if(msg.startswith('!')):
    if message.channel.name != "encourage-bot":
      await message.channel.send("Please only use this bot in <#857856413942153266>")
    elif msg.startswith('!hello' ):
      await message.channel.send("Hello!")
    
    elif msg.startswith('!inspire') :
      await message.channel.send(get_quote())
    
    elif msg.startswith('!new'):
      encouraging_message = msg[5:len(msg)]
      update_encouragements(encouraging_message)
      await message.channel.send("New encouraging message added")
    
    elif msg.startswith('!del'):
      if "encouragements" in db.keys():
        index = int(msg.split(" ")[1])
        print(index)
        delete_encouragment(index)
        encouragements = db["encouragements"]
      await message.channel.send("Encouragement has been delted!")
    
    elif msg.startswith('!list'):
      encouragements = []
      if "encouragements" in db.keys():
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)
    
    elif msg.startswith('!clear'):
      db["encouragements"] = []
      await message.channel.send("Encouragements reset!")
    
    elif msg.startswith('!encourage'):
      if "encouragements" in db.keys():
        await message.channel.send(random.choice(db["encouragements"]))
      else:
        await message.channel.send("There are no encouragements available!")
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(encouragements))

keep_alive()
my_secret = os.environ['token']
client.run(my_secret)