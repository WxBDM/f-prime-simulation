#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import probabilities as prob
from utils import Utils

class CommsState:
    
    '''Process code for Comms state.'''

    utils = Utils()

    def __init__(self, information):
        self.this_state = information['current_state']
        self.probabilities = prob.comms()
        self.previous_state = information['previous_state']
        self.stack = information['stack']
        
        self.util_header = {'previous_state' : self.previous_state,
                            'stack_to_string' : self.stack.to_string(),
                            'current_state' : self.this_state,
                            'probabilities' : self.probabilities
                            }
    
    def phm_flags(self):
        '''Sets the PHM flags for the Comms state.'''
        # DO NOT INCLUDE REACTION WHEEL SATURATION LIMITS! This is hardware
        # based, so they will be checked in the PHM.
        
        # === EDIT THIS DICTIONARY WITH PHM FLAGS FOR THIS STATE ===
        
        flags = {'state' : 'comms'}
        
        # =============================================================
        
        return flags

    def run_process(self):
        '''Driver code to run a simulation for the Comms state.'''
        
		# print out end/start of new state.
        self.utils.header(self.util_header)
        
        # ==== YOUR CODE GOES HERE. ====
        
        
        
        
        # ==============================
        
        print("==== END COMMS ====\n")
        return self.stack
        

# This is the test driver code. Be sure to comment/delete before integrating it
# into the driver code!

# import stack
# information = {'previous_state' : 'START!',
#       'stack' : stack.StateStack(), # just instantiate a new object for now.
#       'current_state' : 'comms'}

# information['previous_state'] = CommsState(information)
# information['previous_state'].run_process()


