#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import probabilities as prob
from utils import Utils

class DisposalState:

    utils = Utils()

    def __init__(self, info):
        self.this_state = info['current_state']
        self.probabilities = prob.disposal()
        self.previous_state = info['previous_state']
        self.stack = info['stack']
        
        self.util_header = {'previous_state' : self.previous_state,
                            'stack_to_string' : self.stack.to_string(),
                            'current_state' : self.this_state,
                            'probabilities' : self.probabilities
                            }

    def run_process(self):
        
		# print out end/start of new state.
        self.utils.header(self.util_header)
        
        # ==== YOUR CODE GOES HERE. ====
        
        
        
        
        # ==============================
        
        print("==== END DISPOSAL ====\n")
        return self.stack
        

# This is the test driver code. Be sure to comment/delete before integrating it
# into the driver code!

# import stack
# information = {'previous_state' : 'START!',
#       'stack' : stack.StateStack(), # just instantiate a new object for now.
#       'current_state' : 'Deployment'}

# charge = DisposalState(information)
# charge.run_process()


