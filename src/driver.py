#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:11:15 2020

The driver file to run the simulation. To edit constraints for the system, 
    see under imports.
    
Note: In order to edit probability constraints of certain events happening,
    go to probability.py.

=== ADDING IN NEW STATES ===
1) Go to command line/terminal, navigate to the directory, type:
        python3 make_stub.py <NAME OF STUB>
    where <NAME OF STUB> is the name you want your state to be.
    
2) Go to probabilities.py and add in a new function with the name of your stub
    with appropriate dictionary values.
    
3) Come to this file, import it (like previous ones)

4) Copy "elif" statement at the bottom of the script, edit approperly,
=============================

@author: bdmolyne
"""

from dstructures.stack import StateStack
from states.charge import ChargeState

import probabilities as prob
from logger_out import logger


class Driver:
    
    def __init__(self, d):
        self.stack = d['stack']
        self.previous_state = d['previous_state']
        self.current_state = d['current_state']
        self.first_itr = True
        self.logger = logger.Logger()
        
    def pack(self):
        return {'stack' : self.stack,
                'previous_state' : self.previous_state,
                'current_state' : self.current_state,
                'logger' : self.logger
                }
    
    def update(self, new_stack):
        
        if len(self.stack) == 0:
            self.current_state = 'None'
        
        else:
            self.previous_state = self.current_state
            
            if len(self.stack) != 0:
                self.current_state = new_stack.pop()
            else:
                self.current_state = 'None'
    
        self.stack = new_stack
        
n_state_transition_cap = 10

# Probilities file check
for probability_d in [prob.warmup(), prob.charge(), prob.deployment(), prob.predisposal(), prob.comms()]:
    for val in list(probability_d.values()):
        if not isinstance(val, int):
            raise ValueError("Probabilites must be integers. Check probabilities.py.")
            
        if not 0 <= val <= 100:
            raise ValueError("There was a value that is not between 0 and 100. Check probabilities.py")


# Initialization
stack = StateStack()
information_d = {'stack' : stack,
                 'previous_state' : 'None',
                 'current_state' : 'Deployment',
                 }
driver = Driver(information_d)

for nth_state in range(n_state_transition_cap):

    if driver.current_state == 'None':
        if driver.first_itr:
            driver.first_itr = False
        else:
            print("State stack is empty. Communicating with ground.")
            break

    if driver.current_state == 'Charge': 
        stack = ChargeState(driver.pack()).run_process()
    
    #elif driver.current_state == 'MYSTATE': 
    #    stack = MYSTATE(driver.pack()).run_process()
    #
    # ...
    
        
    elif len(driver.stack) == 0:
        print("State stack is empty. Communicating with ground.")
        print("Ending.")
        break
    
    else:
        print("Unrecognized state. Stack: {}".format(driver.stack))
        print("Ending")
        break

    driver.update(stack)











