#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:25:15 2020

@author: bdmolyne
"""

import random

class Utils:
    
    def pass_or_fail(self, parameter):
        '''Method to randomly generate a random number for decision logic.
        
        Reads in probabilities set in probabilities.py and generates a random
            number. If the number is greater than the set number, then
            the it will return False (signifying that the diamond failed).
            Otherwise, it will return True, signfiying the diamond passed.
        
        Example: probability = 70. If 71 or higher is generated, it fails.'''
        
        random_n = random.randint(1, 100)
        if parameter < random_n:
            return False
    
        return True 
    
    def convert_yes_no(self, val):
        '''Converts True or False values to Yes or No for UI purposes.'''
        
        if not isinstance(val, bool):
            # devleoper check
            raise ValueError("val must be boolean. Found: {}".format(type(val)))
            return
    
        if val: return 'Yes'
        return 'No'
    
    def header(self, d):
        
         # print out end/start of new state.
        print("State stack: {}".format(d['stack_to_string']))
        print("==== START {} ====".format(d['current_state']))
        
        # print out the probabilities
        print("Probabilities of success for {} state:".format(d['current_state']))
        for param in d['probabilities']:
            print('\t{} = {}%'.format(param, d['probabilities'][param]))
        print()
        
        
        
        
        
        
        
        