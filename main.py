import discord
from discord.utils import get
import os
from keep_alive import keep_alive
from schedule import embedSchedule
from getRoster import getRosterEmbed
from helpfunction import *
from scrollReaction import handleReaction
from webscraper import getStandingsEmbed
from scores import getScoreEmbed
from getTeams import *


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
        if len(message.embeds) > 0:
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

            elif msg.startswith("-teamList"):
              reign = "<:reign:864275520769359882>"
              uprising = "<:uprising:864275585022427157>"
              hunters = "<:hunters:864275450032816168>"
              fuel = "<:fuel:864275397910593536>"
              mayhem = "<:mayhem:864275488473612299>"
              gladiators = "<:gladiators:864275436987744307>"
              charge = "<:charge:864275280985980938>"
              outlaws = "<:outlaws:864275505766334486>"
              spark = "<:spark:864275546498531388>"
              spitfire = "<:spitfire:864275559567196221>"
              excelsior = "<:excelsior:864275362477506590>"
              eternal = "<:eternal:864275341619232808>"
              fusion = "<:fusion:864275415061495839>"
              dynasty = "<:dynasty:864275320675500052>"
              shock = "<:shock:864275535336570912>"
              dragons = "<:dragons:864275306776231948>"
              defiant = "<:defiant:864275293065445396>"
              valiant = "<:valiant:864275597630504970>"
              titans = "<:titans:864275573999927326>"
              justice = "<:justice:864275469510508574>"
              await message.channel.send(embed = getTeams(reign, uprising, hunters, fuel, mayhem, gladiators, charge, outlaws, spark,
              spitfire, excelsior, eternal, fusion, dynasty, shock, dragons, defiant, valiant, titans, justice))

            else:
                if msg.startswith("-owl"):
                    restofmsg = msg.split('-owl ')[1]

                    if restofmsg.startswith('roster'):
                        team = (restofmsg.split("roster ")[1]).lower()
                        await message.channel.send(getRosterEmbed(team))


                    elif restofmsg == "standings":
                        standingsEmbed = getStandingsEmbed(0)
                        # print(len(standingsEmbed))
                        await message.channel.send(embed=standingsEmbed)

                    elif restofmsg == 'schedule':
                        await message.channel.send(embed=embedSchedule())
                    
                    elif restofmsg == 'scores':
                        await message.channel.send(embed=getScoreEmbed())




keep_alive()
my_secret = os.environ['token']
client.run(my_secret)