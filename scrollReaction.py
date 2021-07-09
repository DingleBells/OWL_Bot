from webscraper import getStandingsEmbed

def handleReaction(reaction):
    nameToNum = {'2021 Regular Season':0 , "May Melee Qualifiers" : 1,  'June Joust: Qualifiers':2
        , 'Summer Showdown: Qualifiers' : 3 , 'Countdown Cup: Qualifiers':4}

    tourney = " ".join(reaction.message.embeds[0].title.split()[:-1])
    tourneynum = nameToNum[tourney]
    # print(tourney, tourney in nameToNum, tourneynum, reaction, str(reaction)=="➡", type(reaction), reaction.emoji)
    newtourney = None
    if str(reaction) == "⬅":
        # going backward
        newtourney = tourneynum - 1
        if newtourney == -1:
            newtourney = 4
    elif str(reaction) == "➡":
        # going forward
        newtourney = tourneynum + 1
        if newtourney == 5:
            newtourney = 0
    if newtourney is not None:
        return getStandingsEmbed(newtourney)
    return None
