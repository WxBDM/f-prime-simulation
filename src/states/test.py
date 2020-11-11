#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import probabilities as prob
from utils import Utils

class TestState:
    
    '''Process code for Test state.'''

    utils = Utils()

    def __init__(self, info):
        self.this_state = info['current_state']
        self.probabilities = prob.test()
        self.previous_state = info['previous_state']
        self.stack = info['stack']
        
        self.util_header = {'previous_state' : self.previous_state,
                            'stack_to_string' : self.stack.to_string(),
                            'current_state' : self.this_state,
                            'probabilities' : self.probabilities
                            }
    
    def phm_flags(self):
        '''Sets the PHM flags for the Test state.'''
        # DO NOT INCLUDE REACTION WHEEL SATURATION LIMITS! This is hardware
        # based, so they will be checked in the PHM.
        
        # === EDIT THIS DICTIONARY WITH PHM FLAGS FOR THIS STATE ===
        
        flags = {'state' : 'test'}
        
        # =============================================================
        
        return flags

    def run_process(self):
        '''Driver code to run a simulation for the Test state.'''
        
		# print out end/start of new state.
        self.utils.header(self.util_header)
        
        # ==== YOUR CODE GOES HERE. ====
        
        
        
        
        # ==============================
        
        print("==== END TEST ====\n")
        return self.stack
        

# This is the test driver code. Be sure to comment/delete before integrating it
# into the driver code!

# import stack
# information = {'previous_state' : 'START!',
#       'stack' : stack.StateStack(), # just instantiate a new object for now.
#       'current_state' : 'Deployment'}

# info['previous_state'] = TestState(information)
# info['previous_state'].run_process()


