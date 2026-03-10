# -*- coding: utf-8 -*-

from classes.class_dungeon_room_door import DungeonRoomDoor
from classes.class_event_based_mission import EventBasedMission
from classes.class_individual_mission import IndividualMission
from classes.class_item_mission import ItemMission
from classes.class_location_based_mission import LocationBasedMission
from classes.class_overview_location import OverviewLocation
from classes.class_purpose_approach import PurposeApproach

class Tables:
    
    # ---------------------------------
    # Generate all random table classes
    # ---------------------------------
    overview_location = OverviewLocation()
    purpose_approach = PurposeApproach()    
    individual_mission = IndividualMission()    
    item_mission = ItemMission()
    location_based_mission = LocationBasedMission()
    event_based_mission = EventBasedMission() 
    dungeon_room_door = DungeonRoomDoor()


    def __init__(self):
        pass
    