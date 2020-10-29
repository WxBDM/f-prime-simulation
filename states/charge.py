#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:56:26 2020

@author: bdmolyne
"""

import probabilities as prob
from utils import Utils

class ChargeState:
    
    utils = Utils()

    def __init__(self, info):
        self.this_state = 'Charge'
        self.probabilities = prob.charge()
        self.previous_state = info['previous_state']
        self.stack = info['stack']
        
        self.util_header = {'previous_state' : self.previous_state,
                       'stack_to_string' : self.stack.to_string(),
                       'current_state' : self.this_state,
                       'probabilities' : self.probabilities
                       }

    def _pack(self):
        '''Packs information to be sent to another function in a dictionary.
        
        Returns:
            dictionary => information regarding the given state.
        '''
        d = { 'stack' : self.stack,
            'probabilities' : self.probabilities,
            'current_state' : self.this_state,
            'is_info_d' : True,
            }
        
        return d
    
    def _add_to_stack(self, states, indent = 0):
        
        # figure out the number of indents
        indent_format = ""
        for i in range(indent):
            indent_format += "\t"
        
        # print information
        print("{}Stack before: {}".format(indent_format, self.stack.to_string()))
        self.stack.push(states)
    
    def phm_flags(self):
        
        d = {'state' : 'Charge',
            'rotation_x' : (None, 5), 
             'rotation_y' : (None, 5),
             'rotation_z' : (None, 5),
             'soc' : (16, None),
             'thermal' : (-10, None),
              }
        
        return d
        
    def run_process(self):
        '''Runs the charge state process. return self.stack out of this function
        means we're going to check the state queue.'''
        
        # print out end/start of new state.
        self.utils.header(self.util_header)
        
        # start logic
        # TSP
        print("\nEstablishing thermal set point")
        print("\tRunning init program")
        print('\tChecking TSP functionality')
        
        # TSP diamond
        tsp_diamond = self.utils.pass_or_fail(self.probabilities['tsp_functionality'])
        if not tsp_diamond: # if it failed
            print("\ttsp functionality failed.")
            print("\tStack before: {}".format(self.stack.to_string()))
            self.stack.push('Charge', indent = 1)
            self.stack.push('Safety 1', indent = 1)
            print("\t" + self.stack.to_string())
            
            print("==== END CHARGE ====\n")
            return self.stack # check state queue
        
        # tsp functionality verified
        print('\ttsp functionality verified')
        
        # set phm flags
        print('Setting PHM flags')
    
        # read optimal charge vector
        print('Reading optimal charge vector')
    
        # check to see if gnc periphs are on.
        gnc_diamond = self.utils.pass_or_fail(self.probabilities['gnc_peripherials_on'])
        gnc_check = self.utils.convert_yes_no(gnc_diamond)
        print("GN&C Periphreal Check: Peripherals {}".format(gnc_check))
        
        # the diamond failed, turning on peripherals
        if not gnc_diamond: #need to initalize them
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
                print("\t\tStack before: {}".format(self.stack.to_string()))
                self.stack.push('Charge', indent = 2)
                self.stack.push('Safety 1', indent = 2)
                print("\t\t" + self.stack.to_string())
                
                print("==== END CHARGE ====\n")
                return self.stack # check state queue
            
            print("\tPeriphreal functionality verified.")
        
        battery_diamond = self.utils.pass_or_fail(self.probabilities['batteries_connected'])
        battery_check = self.utils.convert_yes_no(battery_diamond)
        print('Battery connection check: {}'.format(battery_check))
        
        if not battery_diamond:
            print("\tBattery isn't connected.")
            print("\t\tStack before: {}".format(self.stack.to_string()))
            self.stack.push('Charge', indent = 2)
            self.stack.push('Safety 1', indent = 2)
            print("\t\t" + self.stack.to_string())
            
            print("==== END CHARGE ====\n")
            return self.stack # check state queue
        
        # Start pointing at the sun
        print("Acquiring sun position")
        print("Initializing sun pointing algorithm")
        print("Now pointing at sun.")
        print("Charging...")
        print("Charge threshold met.")
        
        print("==== END CHARGE ====\n")
        return self.stack

# test driver code, delete when scaling.
import sys, os
sys.path.append(os.path.dirname(os.getcwd())) # 'location_of_project/f-prime-simulation'

from dstructures.stack import StateStack

information = {'previous_state' : 'START!',
                'stack' : StateStack(), # just instantiate a new object for now.
                'current_state' : 'Charge'}

charge = ChargeState(information)
charge.run_process()








