#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:56:26 2020

@author: bdmolyne
"""

import probabilities as prob
from utils import Utils

class ChargeState:
    
    utils = Utils()

    def __init__(self, info):
        self.this_state = 'Charge'
        self.probabilities = prob.charge()
        self.previous_state = info['previous_state']
        self.stack = info['stack']
        
        self.util_header = {'previous_state' : self.previous_state,
                       'stack_to_string' : self.stack.to_string(),
                       'current_state' : self.this_state,
                       'probabilities' : self.probabilities
                       }

    def _pack(self):
        '''Packs information to be sent to another function in a dictionary.
        
        Returns:
            dictionary => information regarding the given state.
        '''
        d = { 'stack' : self.stack,
            'probabilities' : self.probabilities,
            'current_state' : self.this_state,
            'is_info_d' : True,
            }
        
        return d
    
    def _add_to_stack(self, states, indent = 0):
        
        # figure out the number of indents
        indent_format = ""
        for i in range(indent):
            indent_format += "\t"
        
        # print information
        print("{}Stack before: {}".format(indent_format, self.stack.to_string()))
        self.stack.push(states)
    
    def phm_flags(self):
        
        d = {'state' : 'Charge',
            'rotation_x' : (None, 5), 
             'rotation_y' : (None, 5),
             'rotation_z' : (None, 5),
             'soc' : (16, None),
             'thermal' : (-10, None),
              }
        
        return d
        
    def run_process(self):
        '''Runs the charge state process. return self.stack out of this function
        means we're going to check the state queue.'''
        
        # print out end/start of new state.
        self.utils.header(self.util_header)
        
        # ==== YOUR CODE GOES HERE. ====
        
        self.events.charge_establish_tsp_init_program()
        # Is TSP working properly?
        passed = self.decisions.charge_tsp_functionally_verified()
        if not passed: # it failed
            # Go into safety and check the state stack.
            self.events.add_state_to_state_stack('charge')
            self.events.add_state_to_state_stack('safety1')
            self.events.check_state_stack()
            return # Whenever you have the above line, REMEMBER TO INCLUDE THIS!
        
        # If it passed, continue this logic (set phm flags)
        self.events.set_phm_flags()
        self.events.read_optimal_charge_vector()
        
        # Are the peripherals on?
        passed = self.decisions.charge_gnc_peripherals_on()
        if not passed:
            self.events.turn_peripherals_on()
            # Check to make sure they're on.
            passed = self.decisions.charge_peripherals_functionally_verified()
            if not passed:
                # Go into safety 1.
                self.events.add_state_to_state_stack('charge')
                self.events.add_state_to_state_stack('safety1')
                self.events.check_state_stack()
                return 
        
        # All is good, point towards the sun and charge.
        self.events.alg_acquire_sun_position_init()
        self.events.alg_sun_pointing_init()
        self.events.charge()
        self.events.alg_sun_pointing_terminate()
        
        self.events.check_state_stack()
        return # this return statement is optional.
    
        # ==============================

# test driver code, delete when scaling.
import sys, os
sys.path.append(os.path.dirname(os.getcwd())) # 'location_of_project/f-prime-simulation'

from dstructures.stack import StateStack

information = {'previous_state' : 'START!',
                'stack' : StateStack(), # just instantiate a new object for now.
                'current_state' : 'Charge'}

charge = ChargeState(information)
charge.run_process()








