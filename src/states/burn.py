#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import probabilities as prob
from utils import Utils
from events import Events, Decisions

class BurnState:
    
    '''Process code for Burn state.'''

    utils = Utils()
    events = Events()

    def __init__(self, info):
        self.this_state = info['current_state']
        self.probabilities = prob.burn()
        self.previous_state = info['previous_state']
        self.stack = info['stack']
        
        self.util_header = {'previous_state' : self.previous_state,
                            'stack_to_string' : self.stack.to_string(),
                            'current_state' : self.this_state,
                            'probabilities' : self.probabilities
                            }
        
        self.decisions = Decisions(self.probabilities)
    
    def phm_flags(self):
        '''Sets the PHM flags for the Burn state.'''
        # DO NOT INCLUDE REACTION WHEEL SATURATION LIMITS! This is hardware
        # based, so they will be checked in the PHM.
        
        # === EDIT THIS DICTIONARY WITH PHM FLAGS FOR THIS STATE ===
        
        flags = {'state' : 'burn',
                 'state_of_charge' : (16, None),
                 'thermal' : (-10, 40),
                 'rotation_x' : (0, 5)
                }
        
        # =============================================================
        
        return flags

    def run_process(self):
        '''Driver code to run a simulation for the Burn state.'''
        
		# print out end/start of new state.
        self.utils.header(self.util_header)
        
        # ==== YOUR CODE GOES HERE. ====
        
        self.events.burn_run_init_program()
        init = self.decisions.burn_tsp_functionally_verified()
        if not init:
            self.events.burn_add_warmup_to_queue()
            self.events.burn_add_safety_1_to_queue()
            return
        
        self.events.burn_set_phm_flags()
        self.events.burn_initiate_pointing_algorithm()
        self.events.burn_turn_thruster_on()
        self.events.burn_burn_it()
        # asssume watchdog timer doesn't kick, skip diamond.
        self.events.burn_turn_thruster_off()
        self.events.burn_terminate_pointing_algorithm()
        
        # ==============================
        
        print("==== END BURN ====\n")
        return self.stack
        

# This is the test driver code. Be sure to comment/delete before integrating it
# into the driver code!

import sys, os
sys.path.append(os.path.dirname(os.getcwd())) # 'location_of_project/f-prime-simulation'
from dstructures.stack import StateStack

information = {'previous_state' : 'START!',
      'stack' : StateStack(), # just instantiate a new object for now.
      'current_state' : 'burn'}

information['previous_state'] = BurnState(information)
information['previous_state'].run_process()

