#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:20:50 2020

@author: bdmolyne
"""

import probabilities as prob
import stack
from utils import Utils

class WarmupState:
    
    utils = Utils()
    
    def __init__(self, info):
        self.this_state = 'Warmup'
        self.probabilities = prob.warmup()
        self.stack = info['stack']
        
        self.util_header = {'previous_state' : info['prev_state'],
                       'stack_to_string' : self.stack.to_string(),
                       'current_state' : self.this_state,
                       'probabilities' : self.probabilities}

    
    def run_process(self):
        '''Runs the warmup state process. return self.stacking out of this function
        means we're going to check the state queue.'''
        
        # Prints the header.
        self.utils.header(self.util_header)
        
        print("Hard reset; turned off all components.")
        print("Initializing OBC")
        print("\tRunning init program")
        print('\tMultistage sequence boot')
        
        print("Initializing EPS")
        print("\tRunning init program")
        print("\tEPS boot sequence")
        print("\tEstablish rail power")
        print('\tChecking EPS functionality')
        
        # Initializing EPS
        eps_diamond = self.utils.pass_or_fail(self.probabilities['eps_functionality'])
        if not eps_diamond: # if it failed
            print("\tEPS functionality failed.")
            self.stack.add_to_state_stack(['Warmup', 'Safety 1'], indent = 1)
            
            print("==== END WARMUP ====\n")
            return self.stack # check state queue
       
        print("\tEPS functionality OK")
        
        # Establishing Thermal Set Point
        print("Establishing thermal set point")
        print("\tRunning init program")
        print('\tChecking TSP functionality')
        
        tsp_diamond = self.utils.pass_or_fail(self.probabilities['tsp_functionality'])
        if not tsp_diamond: # if it failed
            print("\tTSP functionality failed.")
            self.stack.add_to_state_stack(['Warmup', 'Safety 1'], indent = 1)
            
            print("==== END WARMUP ====\n")
            return self.stack # check state queue

        print("\tTSP functionality OK")
        
        print("Setting PHM flags")
    
        # Watchdog startup
        print("Watchdog Startup")
        print("\tInitalizing watchdog timers")
        print('\tChecking timer functionality')
        watchdog_diamond = self.utils.pass_or_fail(self.probabilities['watchdog_functionality'])
        if not watchdog_diamond: # if it failed
            print("\tWatchdog timer functionality failed.")
            self.stack.add_to_state_stack(['Warmup', 'Safety 1'], indent = 1)
            
            print("==== END WARMUP ====\n")
            return self.stack # check state queue
        
        # Initialize peripherals
        print("Initializing Peripherals.")
        rw_init = self.utils.pass_or_fail(self.probabilities['rw_functionality'])
        print("\tInitializing RW")
        imu_init = self.utils.pass_or_fail(self.probabilities['imu_functionality'])
        print("\tInitializing IMU")
        st_init = self.utils.pass_or_fail(self.probabilities['st_functionality'])
        print("\tInitializing ST")
        ss_init = self.utils.pass_or_fail(self.probabilities['ss_functionality'])
        print("\tInitializing SS")
        
        if not all([rw_init, imu_init, st_init, ss_init]):
            print("\tOne failed functionality.")
            self.stack.add_to_state_stack(['Warmup', 'Safety 1'], indent = 1)
            
            print("==== END WARMUP ====\n")
            
            return self.stack # check state queue
    
        # RW Desaturation
        print("Checking RW wheel near saturation limit.")
        rw_desat = self.utils.pass_or_fail(self.probabilities['any_rw_near_saturation'])
        if not rw_desat: # if it failed, check stack.
            print("\tRW near saturation limit.")
            print("\tChecking state stack.")
            if "RW Desaturation" in self.stack:
                print("\t\tRW Desaturation in stack.")
                
            else:
                print("\t\tRW Desaturation not in stack")
                self.stack.add_to_state_stack('RW Desaturation', indent = 2)
        
            print("Initiating warm-up sequence")
            print("Enough propellant is liquid.")
            
            print("==== END WARMUP ====\n")
            
            return self.stack
        
        # RW not near saturation limit.
        print("Reading optimal charge vector")
        print("Acquiring sun position")
        print("Initiaing sun pointing algorithm")
        print("Initianting warmup sequence")
        print("Enough propellent is liquid")
        print("Terminating sun pointing algorithm")
    
        # Burn power check
        soc_above_burn_thresh = self.utils.pass_or_fail(self.probabilities['soc_above_burn_threshold'])
        soc_abv_burn_thresh_english = self.utils.convert_yes_no(soc_above_burn_thresh)
        print("SoC above burn thresh? {}".format(soc_abv_burn_thresh_english))
        if not soc_above_burn_thresh: #red line
            self.stack.add_to_state_stack(['Warmup', 'Charge'], indent = 1)
        
        print("==== END WARMUP ====\n")
        
        return self.stack


# # test driver code, delete when scaling.
# information = {'prev_state' : 'START!',
#                'stack' : stack.StateStack() # just instantiate a new object for now.
#                }

# charge = WarmupState(information)
# charge.run_process()








