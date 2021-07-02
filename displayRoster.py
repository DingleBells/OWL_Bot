from roster import *
import discord
import os
def findTeam(team):
  final = "";
  if team == 'atlanta reign' or team == 'reign':
    final = final + "```Atlanta Reign roster\n"
    final = final + str(getAtlantaRoster()+'```')
    return final
  
  elif team == 'boston uprising' or team == 'uprising':
    return str(getBostonRoster())

  elif team == 'chengdu hunters' or team == 'hunters':
    return str(getChengouRoster())
  
  elif team == 'dallas fuel' or team == 'fuel':
    return str(getDallasRoster())
  
  elif team == 'florida mayhem' or team == 'mayhem':
    return str(getFloridaRoster())
  
  elif team == 'guangzhou charge' or team == 'charge':
    return str(getGuangzhouRoster())
  
  elif team == 'hangzhou spark' or team == 'spark':
    return str(getHangzhouRoster())
  
  elif team == 'houston outlaws' or team == 'outlaws':
    return str(getHoustonRoster())
  
  elif team == 'london spitfire' or team == 'spitfire':
    return str(getLondonRoster())
  
  elif team == 'los angeles gladiators' or team == 'gladiators':
    return str(getLAGRoster())
  
  elif team == 'los angeles valiant' or team == 'valiant':
    return str(getLAVRoster())
  
  elif team == 'new york excelsior' or team == 'excelsior':
    return str(getNYRoster())
  
  elif team == 'paris eternal' or team == 'eternal':
    return str(getParisRoster())
  
  elif team == 'philadelphia fusion' or team == 'fusion':
    return str(getPhiladelphiaRoster())
  
  elif team == 'san francisco shock' or team == 'shock':
    return str(getSFSRoster())
  
  elif team == 'seoul dynasty' or team == 'dynasty':
    return str(getSeoulRoster())
  
  elif team == 'shanghai dragons' or team == 'dragons':
    return str(getShanghaiRoster())
  
  elif team == 'toronto defiant' or team == 'defiant':
    return str(getTorontoRoster())
  
  elif team == 'vancouver titans' or team == 'titans':
    return str(getVancouverRoster())
  
  elif team == 'washington justice' or team == 'justice':
    return str(getWashingtonRoster())
  
  else:
    return "That is not an Overwatch League Team"