#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:07:35 2020

@author: bdmolyne
"""

class PHM:
    '''Prognostic Health Managemet system. The PHM flags are represented
    as a dictionary. Every time a new set of flags are set, the dictionary
    is cleared.'''
    
    def __init__(self, list_of_states):
        self.phm_flags = {}
    
    
    def set_flags(self, which_state):
        self.phm_flags = {}