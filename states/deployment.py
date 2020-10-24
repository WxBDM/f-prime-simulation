#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:16:33 2020

Simulation of the deployment phase.

@author: bdmolyne
"""

import probabilities as prob
from utils import Utils

class DeploymentState:
    
    utils = Utils()
    
    def __init__(self, info):
        self.this_state = info['current_state']
        self.probabilities = prob.deployment()
        self.previous_state = info['previous_state']
        self.stack = info['stack']
        
        self.util_header = {'previous_state' : self.previous_state,
                       'stack_to_string' : self.stack.to_string(),
                       'current_state' : self.this_state,
                       'probabilities' : self.probabilities
                       }

    def run_process(self):
        # If the boolean is True, we go into emergency comms.
        emergency_needed = False
        
        # print out end/start of new state.
        self.utils.header(self.util_header)
        
        print("Deployment detected.")
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
            print("\tSaving to contingency ledger.")
            emergency_needed = True
        else:
            print("\tEPS functionality OK")
        
        # Establishing Thermal Set Point
        print("Establishing thermal set point")
        print("\tRunning init program")
        print('\tChecking TSP functionality')
        
        tsp_diamond = self.utils.pass_or_fail(self.probabilities['tsp_functionality'])
        if not tsp_diamond: # if it failed
            print("\ttsp functionality failed.")
            print("\tSaving to contingency ledger.")
            emergency_needed = True
        else:
            print("\tTSP functionality OK")
    
        # Watchdog startup
        print("Watchdog Startup")
        print("\tInitalizing watchdog timers")
        print('\tChecking timer functionality')
        watchdog_diamond = self.utils.pass_or_fail(self.probabilities['watchdog_functionality'])
        if not watchdog_diamond: # if it failed
            print("\Watchdog timer functionality failed.")
            print("\tSaving to contingency ledger.")
            emergency_needed = True
        else:
            print("\tWatchdog functionality OK")
        
        # SoC is above detumble threshold
        print("SoC is above detumble threshold.")
        
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
            print("\tSaving to contingency ledger.")
            emergency_needed = True
        else:
            print("\tPeriphreal functionality verified.")
        
        # Detumble and deploy.
        print("Initializing detumble functionality")
        print("Solar pannel 1, 2, and 3 deployed.")
        print("Checking for non-standard burn wire signals")
        burn_wire = self.utils.pass_or_fail(self.probabilities['recieved_non_standard_burn_wire_signal'])
        if not burn_wire:
            print("\tNon-standard burn wire signal detected.")
            print("\tSaving to contingency ledger.")
            emergency_needed = True
        else:
            print("\tBurn wire signal OK.")
            
        print("Terminating detumble functionality")
        
        #emergency comms
        if emergency_needed:
            print("Emergency comms needed.")
            print("\tRF Inhibit over.")
            print("\tStack before: {}".format(self.stack.to_string()))
            self.stack.push('Contingency', indent = 1)
            print("\t" + self.stack.to_string())
            
            print("==== END DEPLOYMENT ====\n")
            return self.stack # check state queue
        
        # set phm flags (don't need emergency comms.)
        print("Setting PHM flags")
        
        # SoC above burn thresh?
        soc_above_burn = self.utils.pass_or_fail(self.probabilities['soc_above_burn_thresh'])
        soc_above_burn_check = self.utils.convert_yes_no(soc_above_burn)
        print('SoC Above burn thresh? {}'.format(soc_above_burn_check))
        if not soc_above_burn:
            print("\tStack before: {}".format(self.stack.to_string()))
            self.stack.push('Comms', indent = 1)
            self.stack.push('Charge', indent = 1)
            print("\t" + self.stack.to_string())
            
            print("==== END DEPLOYMENT ====\n")
            return self.stack # check state queue
        
        # Charge rate positive?
        charge_rate_pos = self.utils.pass_or_fail(self.probabilities['charge_rate_positive'])
        charge_rate_pos_check = self.utils.convert_yes_no(charge_rate_pos)
        print('Charge rate positive? {}'.format(charge_rate_pos_check))
        if not charge_rate_pos:
            print("\tStack before: {}".format(self.stack.to_string()))
            self.stack.push('Comms', indent = 1)
            self.stack.push('Charge', indent = 1)
            print("\t" + self.stack.to_string())
            
            print("==== END DEPLOYMENT ====\n")
            return self.stack # check state queue
        
        # last triangle RF inhibit
        print("RF Inhibit over.")
        self.stack.push('Comms', indent = 0)
        print("\t" + self.stack.to_string())
        
        print("==== END DEPLOYMENT ====\n")
        
        return self.stack # check state queue


# # test driver code, delete when scaling.

# import sys, os
# sys.path.append(os.path.dirname(os.getcwd())) # 'location_of_project/f-prime-simulation'
# from dstructures.stack import StateStack

# information = {'previous_state' : 'START!',
#                'stack' : StateStack(), # just instantiate a new object for now.
#                'current_state' : 'Deployment'}

# charge = DeploymentState(information)
# charge.run_process()




