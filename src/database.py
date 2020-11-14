#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 08:44:22 2020

@author: bdmolyne
"""

import pandas as pd

class Database:

    def __init__(self, phm_mgr_obj, hardware_mgr_obj, states_mgr_obj):
        self.phm = phm_mgr_obj
        self.hardware = hardware_mgr_obj
        self.states = states_mgr_obj

    def to_csv(self):
        pass        
    
    def components_to_series(self):
        
        '''Takes all databases and combines them into a series'''
        
        components = [self.phm, self.hardware, self.states]
        
        d = {}
        for component in components:
            names = component.db['name'].to_list()
            cols = list(component.db.columns)
            
            row_index = 0
            for row in names:
                for column in cols:
                    
                    if column == 'name': continue
                
                    global_df_col_name = "_".join([component.mgr_type, row, column])
                    val = component.db.iloc[row_index][column]
                    d[global_df_col_name] = val
                
                row_index += 1
    
        return pd.Series(data = d)