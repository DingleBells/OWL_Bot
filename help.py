import discord

def getHelp():
  helpScreen = discord.Embed(
    title = "All commands",
    description = "List of all commands and functions",
    color = discord.Colour.gold()
  )

  helpScreen.add_field(name = "-owl shedule", value = "Gets the schedule for the current week in PST")

  helpScreen.add_field(name = "-roster {team name}", value = "Gets the roster for a given team name. Please type out the full team name")

  return helpScreen