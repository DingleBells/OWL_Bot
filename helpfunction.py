import discord


def getHelp():
    helpScreen = discord.Embed(
        title="All commands for bot",
        description="List of all commands and functions",
        color=discord.Colour.gold()
    )

    helpScreen.add_field(name="OWL Commands: ", value="Type: -help owl")

    helpScreen.add_field(name="Other Commands: ",
                         value="Type: -help general")

    return helpScreen

def getOWLHelp():
    helpScreen = discord.Embed(
        title="All OWL-related Commands",
        color=discord.Colour.gold()
    )
    helpScreen.add_field(name='-owl get roster {team name}', value='Get the current roster of an Overwatch League Team.')
    helpScreen.add_field(name='-owl schedule', value="Get the Overwatch League's schedule for the week.")
    helpScreen.add_field(name='-owl standings {number}', value='Get the standings for an Overwatch League Tournament;'
                    '0 for Reg. Season, 1 for May Melee, 2 for June Joust, 3 for Summer Showdown, 4 for Countdown Cup ')
    return helpScreen

def getGeneralHelp():
    helpScreen = discord.Embed(
        title="Other Miscellaneous Comamnds",
        color=discord.Colour.gold()
    )

    helpScreen.add_field(name="-settings whitelist {channnel} ", value="Whitelist a channel for OWL Bot commands")
    helpScreen.add_field(name="-settings get whitelist: ", value="Get the whitelisted channels")
    helpScreen.add_field(name="-settings clear whitelist", value='Clear the list of whitelisted channels')
    return helpScreen


def isChannelGood(channel):
    f = open("channels.txt")
    channel = str(channel)
    for line in f.readlines():
        # print(channel, line.strip(), type(channel), type(line))
        if channel == line.strip():
            f.close()
            return True
    f.close()
    return False

def getGoodChannels():
    f = open('channels.txt')
    outlist = []
    for line in f.readlines():
        outlist.append(line.strip())
    return outlist

def addGoodChannel(channel):
    f = open("channels.txt", 'a')
    f.write(f"{channel}\n")
    f.close()
    return

def clearGoodChannels():
    open('channels.txt', 'w').close()