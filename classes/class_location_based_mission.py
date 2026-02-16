# -*- coding: utf-8 -*-
import random

class LocationBasedMission:
    
    part_01 = [
        "Assault","Break siege of", "Capture and hold", 
        "Defend from attack at", "Destroy",  "Escape from",  
        "Explore", "Find or locate", "Get supplies to", 
        "Infiltrate and control", "Infiltrate and spy upon", 
        "Liberate", "Locate spy at", "Locate intruder at",
        "Loot", "Protect from infiltration at", "Reinforce", 
        "Rescue hostages from", "Retake", 
        "Secretly return something to", "Stage raid upon" 
        ]

    part_02 = [
        "an archaeological dig", 
        "a caravan", 
        "a castle", 
        "the caves", 
        "a cottage",
        "a dungeon",  
        "an encampment", 
        "an extra-planar area", 
        "a flying Structure", 
        "a flying Vehicle", 
        "a forest", 
        "a fort", 
        "a fortified building",
        "a manor", 
        "a grove",  
        "an oasis", 
        "a prison", 
        "the ruins", 
        "a ship",
        "a stockade",
        "a swamp", 
        "a tavern",  
        "a temple",
        "a village",  
        "a warehouse", 
        "the wharfs",
        "the docks" 
        ]


    
    def __init__(self):
        pass



    def getResult(self):
        a = random.randint(0, len(self.part_01) - 1)
        b = random.randint(0, len(self.part_02) - 1)
        return self.part_01[a] + " " + self.part_02[b]
        