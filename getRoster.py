from showRoster import *
import discord
import os
def findTeam(team):
  final = "";
  if(contains(team) == 1):
    return "```"+team+" roster\n"+getRoster(team.split(" ")[1])+"```"
  
  elif(containsLast(team) == 1):
    return "```"+team+" roster\n"+getRoster(team)+"```"
  

def contains(team):
  team_names = ['atlanta reign','boston uprising','dallas fuel',
  'florida mayhem','guangzhou charge','hangzhou spark','houston outlaws',
  'london spitfire','los angeles gladiators','los angeles valiant',
  'new york excelsior','paris eternal','philadelphia fusion',
  'san francisco shock', 'seoul dynasty','shanghai dragons',
  'toronto defiant', 'vancouver titans','washington justice']

  for teams in team_names:
    if(teams == team):
      return 1
  
  return 0

def containsLast(team) :
  team_names = ['reign','uprising','fuel',
  'mayhem','charge','spark','outlaws',
  'spitfire','gladiators','valiant',
  'excelsior','eternal','fusion',
  'shock', 'dynasty','dragons',
  'defiant', 'titans','justice']

  for teams in team_names:
    if(teams == team):
      return 1
  
  return 0