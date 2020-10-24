#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import probabilities as prob
from utils import Utils

class CommsState:

    utils = Utils()

    def __init__(self, info):
        self.this_state = info['current_state']
        self.probabilities = prob.comms()
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
        
        # Establishing Thermal Set Point
        print("Establishing thermal set point")
        print("\tRunning init program")
        print('\tChecking TSP functionality')
        
        tsp_diamond = self.utils.pass_or_fail(self.probabilities['tsp_functionality'])
        if not tsp_diamond: # if it failed
            print("\tTSP functionality failed.")
            self.stack.add_to_state_stack(['Warmup', 'Safety 1'], indent = 1)
            
            print("==== END COMMS ====\n")
            return self.stack # check state queue
        print("\tTSP functionality success.")
        
        print("Set PHM Flags")
        print("RF Inhibit over.")
        
        # check SoC is above radio power threshold.
        soc_above_radio_thresh = self.utils.pass_or_fail(self.probabilities['soc_above_radio_power_thresh'])
        soc_above_radio_english = self.utils.convert_yes_no(soc_above_radio_thresh)
        print("SoC above radio power threshold? {}".format(soc_above_radio_english))
        if not soc_above_radio_thresh:
            radio_on = self.utils.pass_or_fail(self.probabilities['is_radio_on'])
            radio_on_english = self.utils.convert_yes_no(radio_on)
            print("\tRadio on? {}".format(radio_on_english))
            if not radio_on:
                print("\t\tTurned radio off.")
            
            self.stack.add_to_state_stack(['Comms', 'Charge'], indent = 2)
            
            print("==== END COMMS ====\n")
            return self.stack # check state queue
        
        # soc is above threshold.
        radio_on = self.utils.pass_or_fail(self.probabilities['is_radio_on'])
        radio_on_english = self.utils.convert_yes_no(radio_on)
        print("Radio on? {}".format(radio_on_english))
        if not radio_on:
            print("\tTurn radio on.")
        
        # check to make sure radio works.
        radio_functionality = self.utils.pass_or_fail(self.probabilities['radio_functionally_verified'])
        radio_functionality_english = self.utils.convert_yes_no(radio_functionality)
        print("Radio funcitonality verified? {}".format(radio_functionality_english))
        if not radio_functionality:
            self.stack.add_to_state_stack(['Comms', 'Charge'], indent = 2)
            
            print("==== END COMMS ====\n")
            return self.stack # check state queue
        
        # Check GNC peripherals
        gnc_periph = self.utils.pass_or_fail(self.probabilities['gnc_peripherials_on'])
        gnc_periph_english = self.utils.convert_yes_no(gnc_periph)
        print("Radio funcitonality verified? {}".format(gnc_periph_english))
        if not gnc_periph:
            rw_init = self.utils.pass_or_fail(self.probabilities['rw_functionality'])
            print("\tInitializing RW")
            imu_init = self.utils.pass_or_fail(self.probabilities['imu_functionality'])
            print("\tInitializing IMU")
            st_init = self.utils.pass_or_fail(self.probabilities['st_functionality'])
            print("\tInitializing ST")
            ss_init = self.utils.pass_or_fail(self.probabilities['ss_functionality'])
            print("\tInitializing SS")
            
            # if any of these fail, charge and safety 1
            if not all([rw_init, imu_init, st_init, ss_init]):
                print("\tOne failed functionality.")
                self.stack.add_to_state_stack(['Comms', 'Safety 1'], indent = 2)
                
                print("==== END COMMS ====\n")
                return self.stack # check state queue
            
            print("\tPeriphreal functionality verified.")
        
        print("Initiate point at earth algorithm")
        print("Switch radio to Transmit and Receive Mode")
        print("Do entire Tx/Rx block. Assume all works properly.")
        print("Terminate point at earth.")
        
        print(self.stack)
        
        print("==== END COMMS ====\n")
        return self.stack # check state queue

# This is the test driver code. Be sure to comment/delete before integrating it
# into the driver code!

# import sys, os
# sys.path.append(os.path.dirname(os.getcwd())) # 'location_of_project/f-prime-simulation'
# from dstructures.stack import StateStack

# information = {'previous_state' : 'START!',
# 'stack' : StateStack(), # just instantiate a new object for now.
# 'current_state' : 'Comms'}

# charge = CommsState(information)
# charge.run_process()

