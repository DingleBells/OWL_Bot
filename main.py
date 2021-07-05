import discord
import os
from keep_alive import keep_alive
from schedule import *
from getRoster import *
from helpfunction import *
from getStandings import *
from schedule import*
from getRoster import *
from helpfunction import*;
from getStandings import *;


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if msg.startswith("-help"):
        if msg == '-help':
            await message.channel.send(embed=getHelp())
        elif msg == '-help general':
            await message.channel.send(embed=getGeneralHelp())
        elif msg == '-help owl':
            await message.channel.send(embed=getOWLHelp())


    elif msg.startswith("-"):
        if msg.startswith("-settings"):
            restofmsg = msg.split('-settings ')[1]
            if restofmsg == "whitelist":
                addGoodChannel(message.channel)
                await message.channel.send("This channel has been whitelisted.")

            elif restofmsg == 'get whitelist':
                await message.channel.send(f"The following channels are whitelisted: {getGoodChannels()}")

            elif restofmsg == 'clear whitelist':
                clearGoodChannels()
                await message.channel.send("The whitelist has been cleared!")

        else:
            if not isChannelGood(message.channel):
                await message.channel.send(":no_entry_sign: This channel cannot be used for OWL commands.")
                return
            else:
                if msg.startswith("-owl"):
                    restofmsg = msg.split('-owl ')[1]

                    if restofmsg.startswith('roster'):
                        team = (restofmsg.split("roster ")[1]).lower()
                        print(team)
                        await message.channel.send(findTeam(team))

                    elif restofmsg.startswith("standings"):
                        response = restofmsg.split()[1]
                        west, east, tourney = owlSchedule(response)
                        print(len(west), len(east))
                        await message.channel.send(tourney)
                        await message.channel.send(west)
                        await message.channel.send(east)

                    elif restofmsg == 'schedule':
                        await message.channel.send(embed=embedSchedule())






keep_alive()
my_secret = os.environ['token']
client.run(my_secret)