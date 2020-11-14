#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from actions import Actions

class TestState:
    
    '''Process code for Test state.'''

    def set_logger(self, logger_obj):
        
        '''Sets the logger object for the class.'''
        
        self.logger = logger_obj
    
    def set_database(self, db_obj):
        
        '''Sets the database object for the class.'''
        
        self._database = db_obj
    
    def get_logger(self):
        
        '''Returns the logger object for the class.'''
        
        return self.logger
    
    def get_database(self):
        
        '''Returns the database object for the class.'''
        
        return self._database
    
    def reset_db_and_logger(self, actions_obj):
        
        '''Resets the database and logger objects for the class.'''
        
        self.logger = actions_obj.logger # gets the logger from the actions class.
        self.db = actions_obj.database
    
    def phm_values(self):
        
        # ==== Edit this dictionary with the values for the Health Management System ====
        # Example: 'satellite_temp' : (-20, 20)
        #   means that the thermometer measuring the satellite temperature 
        #   should not exceed -20C and 20C.
        
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
        '''Driver code to run a simulation for the Test state. This method
        calls methods from the Actions component.'''
        
        self._database.phm.register(self.phm_values())
        self.logger.set_state('test')
        actions = Actions(self.logger, self._database) # instantiates action class, sets logger and db
        actions.probabilities = self.decision_probability()
        
        # ==== vvvv YOUR CODE GOES BELOW THIS vvvv ====

    
        # ==== ^^^^ YOUR CODE GOES ABOVE THIS ^^^^ ====

