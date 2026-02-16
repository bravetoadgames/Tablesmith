# -*- coding: utf-8 -*-
import random

class PurposeApproach:
    
    part_01 = [
        "Ancestral","Awakening","Battle","Betrayal","Binding",
        "Birthing","Black", "Bone","Brain","Breeding",
        "Bridal", "Burial","Cannibal", "Confessional", "Confluent", 
        "Crypt","Curse","Dark", "Death","Demon",
        "Dimensional", "Discord","Dissection", "Draining","Dream",
        "Earth","Ectoplasmic", "Egg", "Entropy", "Entry",
        "Eye","Feeding", "Fever","Filth","Fire",
        "Flesh","Focus","Fossil","Furnace","Gate",
        "Ghoul","Growth","Guard","Harmonic", "Ice",
        "Illusion","Infesting","Killing","Lifting","Lightning",
        "Madness","Malformation","Materialization", "Meat", "Memory",
        "Mind","Minion","Mist","Moon","Mummification", "Murder",
        "Mutation", "Necromantic", "Obedience","Oracle","Outer",
        "Paradoxical", "Pattern", "Perfume","Plague","Pleasure", 
        "Prayer","Prison","Puzzle","Reaction","Rearrangement", 
        "Sacrificial", "Sand","Screaming","Shadow","Shaping",
        "Simulacrum", "Skeleton", "Skin", "Slime","Spell",
        "Spider", "Storm","Teleportation", "Tentacle","Time",
        "Transformational", "Tuning","Unreality","Vision","War",
        "Winter", "Witch","Witching" 
        ]

    part_02 = [
        "Altar","Barge", "Beacon", "Bowl", "Boxes", 
        "Cages", "Cairn", "Camp", "Catalyst", "Caverns", 
        "Cells", "Channel", "Chasm", "Chimney", "Circle", 
        "Cocoons", "Compactor", "Compass", "Connector", "Coops", 
        "Crown", "Dancer", "Device", "Disk", "Docks", "Dome", 
        "Factory", "Farm", "Flowers", "Forge", "Fountain", "Frame", 
        "Gallery", "Game", "Garden", "Globe", "Grounds", 
        "Harbor", "Harvester", "Hatchery", "Hive", "Houses", 
        "Incubator", "Jars", "Kennels", "Keys", "Kiln", 
        "Laboratories", "Lantern", "Lens", "Machine", "Mandala", 
        "Mirror", "Moat", "Nets", "Orb", "Organs", 
        "Ovens", "Pendulum", "Pens", "Perches", "Pillars", 
        "Pipes", "Pits", "Pools", "Portal", "Preserver", 
        "Priests", "Prism", "Quarters", "Rafts", "Rods", "Rooms", 
        "Rune", "Sanctum", "Separator", "Ship", "Sphere", "Spiral", 
        "Spire", "Spouts", "Stage", "Statue", "Steps", "Swamp", 
        "Theater", "Throne", "Token", "Tomb", "Tower", 
        "Traps", "Trees", "Tubes", "Vats", "Vines", 
        "Vortex", "Wards", "Webs", "Well", "Wheel" 
        ]
    
    
    def __init__(self):
        pass



    def getResult(self):
        a = random.randint(0, len(self.part_01) - 1)
        b = random.randint(0, len(self.part_02) - 1)
        return self.part_01[a] + " " + self.part_02[b]
        