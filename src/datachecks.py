#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:22:06 2020

@author: bdmolyne
"""

class DataInputChecks:
    
    '''Class to check the data types of a component's method of the system'''
    
    @staticmethod
    def phm_register(db, data_dict, ma_dict):
        
        '''Checks to ensure that the data being passed into PHM is valid.
        
        **EDIT THIS, IT IS NOW A DICTIONARY!**'''
        
        # Data type checks!
        error_msg = "Be sure to check the configuration file."
        
        # check to make sure it isn't registered already.
        if name in db['name'].to_list():
            raise ValueError("{} is already registered. {}".format(name, error_msg))
        
        # Ensures the name is a string.
        if not isinstance(name, str):
            raise ValueError("arg name must be string. Found: {}. {}".format(type(name), error_msg))
        
        # Ensures ma_dict is a dictionary.
        if not isinstance(ma_dict, dict):
            raise ValueError("arg ma_dict must be a dictionary. Found: {}. {}".format(type(ma_dict), error_msg))
        
        # Ensures bounds is a tuple.
        if not isinstance(bounds, tuple):
            raise ValueError("arg bounds must be tuple. Found: {}. {}".format(type(bounds), error_msg))
        
        # Ensures bounds tuple is length of 2.
        if len(bounds) != 2:
            raise ValueError("arg bounds must be length 2. Found: {}. {}".format(len(bounds), error_msg))
        
        # Ensures that there's a number (or none type) associated with each bound.
        if not isinstance(bounds[0], (float, int, type(None))):
            raise ValueError("First bound invalid; must be int/float. Found: {}. \
                             {}".format(type(bounds[0]), error_msg))
        if not isinstance(bounds[1], (float, int, type(None))):
            raise ValueError("First bound invalid; must be int/float. Found: {}. \
                             {}".format(type(bounds[1]), error_msg))
        
        # Compare the two bounds unless it's a none type.
        if None not in bounds and bounds[0] > bounds[1]:
            raise ValueError("Lower bound greater than upper bound. {}".format(error_msg))
        
        # check to see if all of the values are none.
        if bounds[0] is None and bounds[1] is None:
            raise ValueError("Both bounds can not be None. {}".format(error_msg))
        
        # check the ma_dict values.
        for key in ma_dict:
            if not isinstance(key, str):
                raise ValueError("arg bounds must be length 2. Found: {}. {}".format(len(bounds), error_msg))

    
    @staticmethod
    def actions_add_to_state_stack(state_str):
        
        '''Checks to make sure a string is getting added to the state stack'''
        
        if not isinstance(state_str, str):
            raise ValueError("state_str not string. Found: {}".format(type(state_str)))
    
        
        
        
        
        
        