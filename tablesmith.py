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

print(tables.overview_location.getResult())
print(tables.purpose_approach.getResult())
print(tables.individual_mission.getResult())
