import discord


def getHelp():
    helpScreen = discord.Embed(
        title="All commands",
        description="List of all commands and functions",
        color=discord.Colour.gold()
    )

    helpScreen.add_field(name="-owl shedule", value="Gets the schedule for the current week in PST")

    helpScreen.add_field(name="-roster {team name}",
                         value="Gets the roster for a given team name. Please type out the full team name")

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