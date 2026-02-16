# -*- coding: utf-8 -*-
import random

class ItemMission:
    
    part_01 = [
        "Attack to obtain", "Conceal", "Defend", 
        "Deliver or transport", "Destroy", 
        "Fake existence of", "Find or locate", "Guard or protect", 
        "Hide", "Hijack", "Prevent delivery of", 
        "Prevent sabotage of", "Raid to obtain", "Retake or repossess", 
        "Sabotage", "Salvage from dangerous place", "Smuggle", 
        "Steal from within location", "Steal while in transit", 
        "Swap fake imitation" 
        ]

    part_02 = [
        "body","corpse", "cargo", "cattle","livestock", 
        "clue", "evidence of crime", "evidence of innocence", 
        "gold","jewelry", "magic item", "map", 
        "message","letter", "monster", 
        "mysterious sealed container", "ownership documents", 
        "religious item", "ship", "statue","idol (portable)", 
        "symbol of authority", 
        "unusual animal (familiar, mascot, pet, prize cow, etc.)", 
        "vehicles with cargo", "weapon (siege engine, famous sword, etc)" 
        ]


    
    def __init__(self):
        pass



    def getResult(self):
        a = random.randint(0, len(self.part_01) - 1)
        b = random.randint(0, len(self.part_02) - 1)
        return self.part_01[a] + " " + self.part_02[b]
        