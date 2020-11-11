#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:14:37 2020

@author: bdmolyne
"""

import pandas as pd

class Logger:

    events = pd.DataFrame({})
    
    # === Algorithms ===
    # This would typically be found in the configuration file, but for now it's
    #   hard coded here.
    algs = ['acquire_sun_position', 'sun_pointing']
    # ==================
    

    class Event:
        
        def __init__(self):
            self._df = pd.Series({'string' : None})
            
            # initialize the series for algorithms.
    
        def add_string(self, string):
            '''Adds a string representation to the event. This is required for logging purposes.
            
            Arguments:
                string (str) => String representation of the event.
            
            Returns:
                None.
            '''
            
            # user check: arg is a string.
            if not isinstance(string, str):
                raise ValueError("Adding event string data type wrong. Expected: str. Actual: {}".format(type(string)))
    
            self._df['string'] = string # assign a string to the series.
        
        def initialize_algorithm(self, name_of_algorithm):
            
            # user check: arg is a string.
            if not isinstance(name_of_algorithm, str):
                raise ValueError("name_of_algorithm must be string. Found: {}.".format(type(name_of_algorithm)))
            
            # user check: arg is in algs list.
            if name_of_algorithm not in self.algs:
                raise ValueError("name_of_algorithm not algs. Options: {}".format(', '.join(self.algs)))
            
            
            
    
    def __repr__(self):
        return self.events.to_string()
    
    def create_new_event(self):
        '''Logger method to a new EVENT node'''
        return self.Event()
    
    def add_to_logger(self, item):
        '''Logger method to add to the log for output.'''
        
        # dev check: ensure that the item being added to the logger is an event.
        if not isinstance(item, self.Event):
            raise ValueError("Added event to logger is not of type Logger.Event; recieved: {}".format(type(item)))
        
        # ensure that there is a string representation for the event.
        if item._df['string'] is None:
            raise ValueError("Event must include a string. Call add_string() method to event object before adding.")
        
        self.events = self.events.append(item._df, ignore_index = True) # need to reassign, it's how pandas works.



