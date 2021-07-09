import discord
import os
from keep_alive import keep_alive
from schedule import embedSchedule
from getRoster import *
from helpfunction import *
from scrollReaction import handleReaction
from webscraper import getStandingsEmbed

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.author == client.user:
        if user != client.user:
            # print("{} has reacted to a message.")
            thing = handleReaction(reaction)
            # print("thing", thing)
            if thing is not None:
                await reaction.message.remove_reaction(reaction, user)
                await reaction.message.edit(embed=thing)

@client.event
async def on_message(message):
    if message.author == client.user:
        if "Standings" in message.embeds[0].title:
            # print("added reactions")
            await message.add_reaction(emoji="⬅")
            await message.add_reaction(emoji="➡")
        else:
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
                        # print(team)
                        await message.channel.send(findTeam(team))


                    elif restofmsg == "standings":
                        standingsEmbed = getStandingsEmbed(0)
                        # print(len(standingsEmbed))
                        await message.channel.send(embed=standingsEmbed)

                    elif restofmsg == 'schedule':
                        await message.channel.send(embed=embedSchedule())






keep_alive()
my_secret = os.environ['token']
client.run(my_secret)