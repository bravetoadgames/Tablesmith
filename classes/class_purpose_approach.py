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
        "altar","barge", "beacon", "bowl", "boxes", 
        "cages", "cairn", "camp", "catalyst", "caverns", 
        "cells", "channel", "chasm", "chimney", "circle", 
        "cocoons", "compactor", "compass", "connector", "coops", 
        "crown", "dancer", "device", "disk", "docks", "dome", 
        "factory", "farm", "flowers", "forge", "fountain", "frame", 
        "gallery", "game", "garden", "globe", "grounds", 
        "harbor", "harvester", "hatchery", "hive", "houses", 
        "incubator", "jars", "kennels", "keys", "kiln", 
        "laboratories", "lantern", "lens", "machine", "mandala", 
        "mirror", "moat", "nets", "orb", "organs", 
        "ovens", "pendulum", "pens", "perches", "pillars", 
        "pipes", "pits", "pools", "portal", "preserver", 
        "priests", "prism", "quarters", "rafts", "rods", "rooms", 
        "rune", "sanctum", "separator", "ship", "sphere", "spiral", 
        "spire", "spouts", "stage", "statue", "steps", "swamp", 
        "theater", "throne", "token", "tomb", "tower", 
        "traps", "trees", "tubes", "vats", "vines", 
        "vortex", "wards", "webs", "well", "wheel" 
        ]
    
    
    def __init__(self):
        pass



    def getResult(self):
        a = random.randint(0, len(self.part_01) - 1)
        b = random.randint(0, len(self.part_02) - 1)
        return self.part_01[a] + " " + self.part_02[b]
        