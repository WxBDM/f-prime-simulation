#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 08:44:22 2020

@author: bdmolyne
"""

import pandas as pd

class Database:
    
    """Almost every component in this project inherits this, as this stores the global 
    attributes for the simulation.
    
    When reading through the source code, each component of the simulation (see architecture
    diagram) has its own class. The class sets any global information that is needed
    for the simulation, as well as provide behavior for the components."""
    
    db_phm_df = pd.DataFrame(columns = ['name', 'lower_bound', 'upper_bound'])
    db_hardware_df = pd.DataFrame(columns = ['name', 'is_on'])
    db_states_df = pd.DataFrame({})

    db_events_df = pd.DataFrame({})
    






