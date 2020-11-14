#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from actions import Actions

class SampleState:
    
    '''Process code for Sample state.'''
    
    def __init__(self):
        self.state_name = 'sample'

    def set_logger(self, logger_obj):
        self.logger = logger_obj
    
    def set_database(self, db_obj):
        self.database = db_obj
    
    def get_logger(self):
        return self.logger
    
    def get_db(self):
        return self.database
    
    def phm_values(self):
        
        # ==== Edit this dictionary with the values for the Health Management System ====
        # Example: 'satellite_temp' : (-20, 20)
        #   means that the satellite temperature should not exceed -20C and 20C.
        
        d = {}
        
        # ===============================================================================
        
        return d

    def decision_probability(self):
        
        # ==== Edit this dictionary with the probabilities for the diamond ====
        # Example: 'check_if_computer_is_on' : 100
        #   means that the diamond to check to see if the computer is on will
        #   succeed 100% of the time.
        
        d = {}
        
        # =====================================================================
        
        return d

    def run_process(self):
        '''Driver code to run a simulation for the Sample state. This method
        calls methods from the Actions component.'''
        
        actions = Actions(self.logger, self.database) # instantiates action class, sets logger and db
        actions.phm = self.phm_values()
        actions.probabilities = self.decision_probability()
        
        # ==== vvvv YOUR CODE GOES BELOW THIS vvvv ====

    
        # ==== ^^^^ YOUR CODE GOES ABOVE THIS ^^^^ ====
        
        self.logger = actions.logger # gets the logger from the actions class.


