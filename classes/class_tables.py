# -*- coding: utf-8 -*-

from classes.class_individual_mission import IndividualMission
from classes.class_overview_location import OverviewLocation
from classes.class_purpose_approach import PurposeApproach


class Tables:
    
    # ---------------------------------
    # Generate all random table classes
    # ---------------------------------
    overview_location = OverviewLocation()
    purpose_approach = PurposeApproach()    
    individual_mission = IndividualMission()    
    
    def __init__(self):
        pass
    