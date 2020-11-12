#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:56:26 2020

@author: bdmolyne
"""

from actions import Actions

class ChargeState():
    
    def set_logger(self, logger_obj):
        self.logger = logger_obj
    
    def phm_values(self):
        
        d = {'state' : 'Charge',
            'rotation_x' : (None, 5), 
             'rotation_y' : (None, 5),
             'rotation_z' : (None, 5),
             'soc' : (16, None),
             'thermal' : (-10, None),
              }
        
        return d

    def decision_probability(self):
        
        d = {'tsp_funct_verified' : 100,
             'peripheral_funct_verified' : 0
             }
    
        return d
        
    def run_process(self):
        '''Runs the charge state process.'''
        
        actions = Actions(self.logger) # instantiates action class, sets logger.
        actions.phm = self.phm_values()
        actions.probabilities = self.decision_probability()
        
        actions.charge_run_init_program()
        actions.verify_tsp()
    
        # ==============================
        
        self.logger = actions.logger # gets the logger from the actions class.
    
    def get_logger(self):
        return self.logger

# test driver code, delete when scaling.
# import sys, os
# sys.path.append(os.path.dirname(os.getcwd())) # 'location_of_project/f-prime-simulation'

# from dstructures.stack import StateStack

# information = {'previous_state' : 'START!',
#                 'stack' : StateStack(), # just instantiate a new object for now.
#                 'current_state' : 'Charge'}

# charge = ChargeState(information)
# charge.run_process()





