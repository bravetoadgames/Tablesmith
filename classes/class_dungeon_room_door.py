# -*- coding: utf-8 -*-
import random

class DungeonRoomDoor:
    
    part_01 = [
        "a beaded string curtain",
        "a fabric curtain",
        "adamantine",
        "basalt",
        "brass",        
        ]

    part_02 = [
        "a bone handle", 
        "a carved wooden handle", 
        "a carved wooden knob", 
        "a double-sided iron bolt", 
        "a double-sided iron bolt with a keyed lock", 
        ]

    part_03 = [
        "a crude iron door knocker that is fixed on the outside of the door",
        "hinges that allow the door to swing both directions",
        "a small shuttered window that opens from the inside",
        "a small open window at eye level",
        "a small hole at eye level",
        ]
    
    def __init__(self):
        pass



    def getResult(self):
        a = random.randint(0, len(self.part_01) - 1)
        b = random.randint(0, len(self.part_02) - 1)
        c = random.randint(0, len(self.part_03) - 1)
        return "The door is made of " + self.part_01[a] + ". It has " + self.part_02[b] + " and " + self.part_03[c] + "."
        