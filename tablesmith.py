#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tablesmith

An RPG random table generator for anything you like.

Created on Sun Feb 15 18:17:59 2026

@author: arjeneke

version 0.1

"""

import tkinter as tk
from classes.class_tables import Tables


tables = Tables()

ui = tk.Tk()
ui.title("Tablesmith - Random tables for (solo) tabletop RPG's")
ui.geometry("1280x720")
ui.resizable(False, False)


def setOutput(txt_output):
    label_output.config(text=txt_output)

label_output = tk.Label(ui, text="", font=("Helvetica", 16))
label_output.pack(pady=10)
label_output.place(x = 10, y = 680)

button_overview_location = tk.Button(ui, text="Overview location", command=lambda: setOutput(tables.overview_location.getResult()))
button_overview_location.place(x = 10, y = 10)
button_overview_location.config(width=20, height=0)

button_purpose_approach = tk.Button(ui, text="Purpose of approach", command=lambda: setOutput(tables.purpose_approach.getResult()))
button_purpose_approach.place(x = 10, y = 50)
button_purpose_approach.config(width=20, height=0)

button_individual_mission = tk.Button(ui, text="Individual mission", command=lambda: setOutput(tables.individual_mission.getResult()))
button_individual_mission.place(x = 10, y = 90)
button_individual_mission.config(width=20, height=0)

button_item_mission = tk.Button(ui, text="Item mission", command=lambda: setOutput(tables.item_mission.getResult()))
button_item_mission.place(x = 10, y = 130)
button_item_mission.config(width=20, height=0)

button_location_based_mission = tk.Button(ui, text="Location based mission", command=lambda: setOutput(tables.location_based_mission.getResult()))
button_location_based_mission.place(x = 10, y = 170)
button_location_based_mission.config(width=20, height=0)

button_event_based_mission = tk.Button(ui, text="Event based mission", command=lambda: setOutput(tables.event_based_mission.getResult()))
button_event_based_mission.place(x = 10, y = 210)
button_event_based_mission.config(width=20, height=0)

ui.mainloop()
