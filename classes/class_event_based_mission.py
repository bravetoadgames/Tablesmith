# -*- coding: utf-8 -*-
import random

class EventBasedMission:

    part_01 = [
        "Destroy results of","Escape from  Solve bizarre mystery  arising from",
        "Expose someone involved in",
        "Hide evidence of what  really happened in a recent",
        "Infiltrate group involved in","Infiltrate group involved in",
        "Investigate events of","Investigate events of",
        "Lead","Coordinate","Plan and execute","Prevent",
        "Protect someone involved in","Sabotage",
        "Survive","Overcome","Take leadership in"
        ]

    part_02 = [
        "an archaeological dig","an arena","a gladiatorial battle",
        "an arrest","a trial","an assassination",
        "a cattle drive through a dangerous area","a coronation",
        "a transfer of power","a coup d’etat","a rebellion",
        "a criminal conspiracy","a disruption of ceremony",
        "a duel","an execution","an imprisonment","an exploration",
        "a mapping expedition","a furtive, stealthy raid",
        "a military assault","a murder","an attempted murder",
        "a natural disaster","a swindle","a theft",
        "a trailblazing attempt into new area","treason and aftermath"
        ]



    def __init__(self):
        pass



    def getResult(self):
        a = random.randint(0, len(self.part_01) - 1)
        b = random.randint(0, len(self.part_02) - 1)
        return self.part_01[a] + " " + self.part_02[b]
