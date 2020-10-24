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

test_code_str = '''# information = {'previous_state' : 'START!',
#       'stack' : stack.StateStack(), # just instantiate a new object for now.
#       'current_state' : 'Deployment'}'''
    
stub = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import probabilities as prob
from utils import Utils

class {0}State:

    utils = Utils()

    def __init__(self, info):
        self.this_state = info['current_state']
        self.probabilities = prob.{1}()
        self.previous_state = {2}
        self.stack = info['stack']
        
        {3}
    
    def phm_values(self):
        # DO NOT INCLUDE REACTION WHEEL SATURATION LIMITS! This is hardware
        # based, so they will be checked in the PHM.
        
        phm = {}
        
        return phm

    def run_process(self):
        
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

# charge = {0}State(information)
# charge.run_process()


'''.format(stub_name.capitalize(), stub_name, previous_state_str, util_header_str,
     test_code_str, stub_name.upper())

file = open("{}.py".format(stub_name), 'w')
file.write(stub)
print("Successfully written to {}.py".format(stub_name))
file.close()



