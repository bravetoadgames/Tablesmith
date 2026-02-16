#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tablesmith

An RPG random table generator for anything you like.

Created on Sun Feb 15 18:17:59 2026

@author: arjeneke

version 0.1

"""

from classes.class_tables import Tables

tables = Tables()

print("Overview location:")
print(tables.overview_location.getResult())
print()

print("Purpose of approach:")
print(tables.purpose_approach.getResult())
print()

print("Individual mission:")
print(tables.individual_mission.getResult())
print()

print("Item mission:")
print(tables.item_mission.getResult())
print()

print("Location based mission:")
print(tables.location_based_mission.getResult())
print()
