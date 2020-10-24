#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:23:52 2020

Data structure to hold information regarding decision logic.

@author: bdmolyne
"""

import probabilities as prob
import random

class Decide:
    
    '''Class to decide whether the decision block passes or not and stores
    appropriate information.'''
    
    def __init__(self, probability):
        
        # dev check
        
        if not isinstance(probability, int):
            error_msg = "initialization failed, prob not integer. Possbile fixes: \n" \
                "1: check to make sure probabilities.py has integers\n" \
                "2: ensure that you're passing in info['probabiliites'][<YOUR PARAMETER>].\n" \
                "Got Value: {}, Type: {}".format(probability, type(probability))
            raise ValueError(error_msg)
        
        # generate random number.
        random_n = random.randint(1, 100)
        if prob < random_n:
            self.passed = False
            self.console_equiv = "No"
    
        self.passed = True 
        self.console_equiv = "Yes"
    

def thermal_set_point_verification(info):
    
    # General logic:
    #   1. Check to make sure
    #   2. Initialize verification datastructure

    # dev checks.
    if not isinstance(info, dict):
        raise ValueError("Parameter must be a dictionary.")
    if not info['is_info_d']:
        error_msg = "Be sure this is an info dictionary. Be sure to pass in self._pack()"
        raise ValueError(error_msg)
    
    verify = Decide(info['probabilities'])
    
    pass
    
    # tsp_diamond = self.utils.pass_or_fail(self.probabilities['tsp_functionality'])
    #     if not tsp_diamond: # if it failed
    #         print("\tTSP functionality failed.")
    #         self.stack.add_to_state_stack(['Warmup', 'Safety 1'], indent = 1)
            
    #         print("==== END COMMS ====\n")
    #         return self.stack # check state queue
    #     print("\tTSP functionality success.")

