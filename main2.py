if message.content.startswith("$owl standings"):
  response = message.content.split()[2]
  west, east, tourney = owlSchedule(response)
  print(len(west), len(east))
  await message.channel.send(tourney)
  await message.channel.send(west)
  await message.channel.send(east)