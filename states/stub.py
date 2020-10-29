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

previous_state_str = "info['previous_state']"

util_header_str = """self.util_header = {'previous_state' : self.previous_state,
                            'stack_to_string' : self.stack.to_string(),
                            'current_state' : self.this_state,
                            'probabilities' : self.probabilities
                            }"""

# have to use % here, .format doesn't work.
phm_flag_val = "flags = {'state' : '%s'}" % stub_name
    
test_code_str = '''# information = {'previous_state' : 'START!',
#       'stack' : stack.StateStack(), # just instantiate a new object for now.
#       'current_state' : '%s'}''' % stub_name
    
stub = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import probabilities as prob
from utils import Utils

class {0}State:
    
    \'''Process code for {0} state.\'''

    utils = Utils()

    def __init__(self, info):
        self.this_state = info['current_state']
        self.probabilities = prob.{1}()
        self.previous_state = {2}
        self.stack = info['stack']
        
        {3}
    
    def phm_flags(self):
        \'''Sets the PHM flags for the {0} state.\'''
        # DO NOT INCLUDE REACTION WHEEL SATURATION LIMITS! This is hardware
        # based, so they will be checked in the PHM.
        
        # === EDIT THIS DICTIONARY WITH PHM FLAGS FOR THIS STATE ===
        
        {6}
        
        # =============================================================
        
        return flags

    def run_process(self):
        \'''Driver code to run a simulation for the {0} state.\'''
        
		# print out end/start of new state.
        self.utils.header(self.util_header)
        
        # ==== YOUR CODE GOES HERE. ====
        
        
        
        
        # ==============================
        
        print("==== END {5} ====\\n")
        return self.stack
        

# This is the test driver code. Be sure to comment/delete before integrating it
# into the driver code!

# import stack
{4}

# {2} = {0}State(information)
# {2}.run_process()


'''.format(stub_name.capitalize(), stub_name, previous_state_str, util_header_str,
     test_code_str, stub_name.upper(), phm_flag_val)

file = open("{}.py".format(stub_name), 'w')
file.write(stub)
print("State stub successfully created: {0}. File: {0}.py".format(stub_name))
file.close()



