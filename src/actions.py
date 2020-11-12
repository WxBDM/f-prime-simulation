#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 23:02:27 2020

@author: bdmolyne
"""

import random
from datachecks import DataInputChecks # to check out data type.

class Actions(DataInputChecks):

    # === Built-in methods, these you do NOT need to edit. ===
    
    def __init__(self, logger):
        self.logger = logger
        
    
    def add_state_to_state_stack(self, state_str):
        '''Adds a state to the state stack.
        
        Args:
            Required: state_str (str) => the state in a string.
        '''
        
        # dev check, type checking
        if not isinstance(state_str, str):
            raise ValueError("state_str not string. Found: {}".format(type(state_str)))
        
        event = self.logger.create_new_event() # creates new event node
        event.add_string('Added {} to state queue'.format(state_str)) 
        self.logger.add(event) # adds event to logger.
        self.logger.StateQueue.add(state_str)
    
    def check_state_stack(self):
        '''Pops the current state off the state stack and transitions into the
        next state.'''
        
        # built in component
        event = self.logger.create_new_event() # creates new event node
        event.add_string('Checking state stack for new state.') # adds a string representation
        self.logger.add(event) # adds event to logger.
        self.ogger.StateStack.check() # State stack functionality
    
    def set_phm_flags(self):
        '''Sets the PHM flags for the state it is currently in'''
        
        event = self.logger.create_new_event()
        event.add_string('Setting PHM flags')
        self.logger.PHM.set_flags() # PHM functionality
        self.logger.add(event)
        
    def decide(self, param):
        '''Randomly generate a number to decide if the process passes or not.'''
        
        if param < random.randint(1, 100): 
            return False
        
        return True 
        
    # ========================================================
    # ============= vvvv ADD METHODS BELOW vvvvv =============
    
    def charge_run_init_program(self):
        
        event = self.logger.create_node()
        event.add_string('Running init program')
        self.logger.add(event)
    
    def verify_tsp(self):
        
        desc = self.logger.create_node()
        if_pass = self.decide(0) # hardcoded for now. get values from state.
        if if_pass:
            desc.add_string('TSP Verification passed')
        else:
            desc.add_string('TSP Verification failed.')
        self.logger.add(desc)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    