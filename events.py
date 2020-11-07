#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:11:44 2020

@author: bdmolyne

This file defines all events that occur in the software.

"""

import random
from logger import Logger

class Events(Logger):
    
    # === Built-in methods, these you do NOT need to edit. ===
    
    def add_state_to_state_stack(self, state_str):
        '''Adds a state to the state stack.
        
        Args:
            Required: state_str (str) => the state in a string.
        
        '''
        
        # dev check, type checking
        if not isinstance(state_str, str):
            raise ValueError("state_str not string. Found: {}".format(type(state_str)))
        
        event = Logger.create_new_event() # creates new event node
        event.add_string('Added {} to state queue'.format(state_str)) 
        Logger.add(event) # adds event to logger.
        Logger.StateQueue.add(state_str)
    
    def check_state_stack(self):
        '''Pops the current state off the state stack and transitions into the
        next state.'''
        
        # built in component
        event = Logger.create_new_event() # creates new event node
        event.add_string('Checking state stack for new state.') # adds a string representation
        Logger.add(event) # adds event to logger.
        Logger.StateStack.check() # State stack functionality
    
    def set_phm_flags(self):
        '''Sets the PHM flags for the state it is currently in'''
        
        event = Logger.create_new_event()
        event.add_string('Setting PHM flags')
        Logger.PHM.set_flags() # PHM functionality
        Logger.add(event)
        
    # ========================================================

    def read_opt_charge_vector(self):
        event = Logger.create_new_event() # creates new event node
        event.add_string('Reading optimal charge vector') # adds a string representation
        Logger.add(event) # adds it to the logger.
    
    def charge_establish_tsp_init_program(self):
        event = Logger.create_new_event() # creates new event node
        event.add_string('Initializing TSP') # adds a string representation
        Logger.add(event) # adds it to the logger.
    
    def turn_peripherals_on(self):
        event = Logger.create_new_event()
        event.add_string("Turning on peripherals")

        # Note: at time of writing, these methods don't exist, but it gets the
        #   point across.
        Logger.turn_on_hardware('rw')
        Logger.turn_on_hardware('imu')
        Logger.turn_on_hardware('st')
        Logger.turn_on_hardware('ss')
        
        Logger.add(event)
    
    def alg_acquire_sun_position_init(self):
        event = Logger.create_new_event()
        event.add_string('Acquiring sun position')
        Logger.initiate_algorithm('sun_positioning')
        Logger.add(event)
    
    def alg_acquire_sun_position_terminate(self):
        event = Logger.create_new_event()
        event.add_string('Terminating sun position algorithm')
        Logger.terminate_algorithm('sun_positioning')
        Logger.add(event)
    
    def alg_sun_pointing_init(self):
        event = Logger.create_new_event()
        event.add_string('Initiating sun pointing algorithm')
        Logger.terminate_algorithm('sun_pointing')
        Logger.add(event)
    
    def alg_sun_pointing_terminate(self):
        event = Logger.create_new_event()
        event.add_string('Terminating sun pointing algorithm')
        Logger.terminate_algorithm('sun_pointing')
        Logger.add(event)
    
    def charge(self):
        event = Logger.create_new_event()
        event.add_string("Charging the satellite's batteries")
        Logger.add(event)


class Decisions(Logger):
    
    def __init__(self, probabilities):
        self.n_decisions = 0 # remember to increment after every decision
        
        # dev check, probabilities dictionary check.
        if not isinstance(probabilities, dict):
            raise ValueError("Argument is not dictionary. Found: {}".format(type(probabilities)))
        
        self.prob_dict = probabilities
    
    def decide(self, param):
        '''Randomly generat a number to decide if the process passes or not.'''
        
        random_n = random.randint(1, 100)
        if param < random_n:
            return False
    
        return True 
    
    # ======
    # Below these comments, load all of the diamonds in the diagrams. 
    # Due to versatility, it is recommended to go with a naming convention such as
    # <state>_<decision>
    
    # Each function returns true or false. True if it passed, false if it didn't.
    
    # All probabilites are loaded into this class, so call probabilities dict
    # as such: self.prob_dict['your_probability_var']
    
    # Example decision function:
    # def burn_tsp_functionally_verified(self):
    #     param = self.prob_dict['tsp_functionality']
    #     self.n_decisions += 1 # remember to increment this!!!
    #     #TODO: Add in logger functionality
    #
    #     return self.decide(param)
    
    # These decisions will be then put into the approrpate software state. This
    #   will make reading the state driver code easier.
    
    # VVVVVV === PUT FUCTIONS BELOW THIS LINE === VVVVVV
    
    def charge_tsp_functionally_verified(self):
        decision = Logger.create_new_decision() # creates new event node
        pass_or_no = decision.decide() # decides whether the diamond passes or fails.   
        decision.add_string("TSP Functionally check")    
        Logger.add(decision) # adds to the logger.    
        return pass_or_no

    def charge_peripherals_functionality_verified(self):
        decision = Logger.create_new_decision()
        pass_or_no = decision.decide() # this is saved inside the decision object and will be auto-written
        decision.add_string("Peripherals init check")
        Logger.add(decision)
        return pass_or_no
    
    def charge_gnc_peripherals_on(self):
        decision = Logger.create_new_decision()
        pass_or_no = decision.decide()
        decision.add_string("checking if GNC peripherals on.")
        Logger.add(decision)
        return pass_or_no
    
    
    
    
    
    
    
    
    
    
    
