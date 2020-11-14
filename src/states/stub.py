#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:37:57 2020

Creates a stub for future states.

@author: bdmolyne
"""

import os
import sys

cwd = os.getcwd()

# check to make sure directory and file name is there.
if len(sys.argv) != 2:
    print("Only include 1 name for stub.")
    exit()
    
stub_name = sys.argv[1].lower()

if stub_name + ".py" in list(os.listdir(os.getcwd())):
    print("ERROR: {}.py already in directory.".format(stub_name))
    exit()

# have to use % here, .format doesn't work.
d = "d = {'state' : '%s'}" % stub_name
    
dict_str = 'd = {}'
    
stub = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from actions import Actions

class {0}State:
    
    \'''Process code for {0} state.\'''
    
    def __init__(self):
        self.state_name = '{2}'

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
        
        {1}
        
        # ===============================================================================
        
        return d

    def decision_probability(self):
        
        # ==== Edit this dictionary with the probabilities for the diamond ====
        # Example: 'check_if_computer_is_on' : 100
        #   means that the diamond to check to see if the computer is on will
        #   succeed 100% of the time.
        
        {1}
        
        # =====================================================================
        
        return d

    def run_process(self):
        \'''Driver code to run a simulation for the {0} state. This method
        calls methods from the Actions component.\'''
        
        actions = Actions(self.logger, self.database) # instantiates action class, sets logger and db
        actions.phm = self.phm_values()
        actions.probabilities = self.decision_probability()
        
        # ==== vvvv YOUR CODE GOES BELOW THIS vvvv ====

    
        # ==== ^^^^ YOUR CODE GOES ABOVE THIS ^^^^ ====
        
        self.logger = actions.logger # gets the logger from the actions class.


'''.format(stub_name.capitalize(), 
            dict_str,
            stub_name)

file = open("{}.py".format(stub_name), 'w')
file.write(stub)
print("State stub successfully created: {0}. File: {0}.py".format(stub_name))
file.close()



