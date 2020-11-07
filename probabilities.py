#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:17:59 2020

This file is a configuration file for probabilities for the simulation.
    All probabilities are logged as the percentage for SUCCESS.
    That is, a value of 100 is 100% success, 50 is 50% success, and 0 is 0% success.
    
    Examples: 
        If eps_functionality = 92, there is a 92% chance that the functionaility 
            of the EPS will be successfully verified.
        If is_radio_on = 48, there is a 48% chance that the radio will be on.

    
    Note that RF inhibit is ALWAYS assumed to be over for simulation speed
        purposes.
    
Each constraint is paired together with the associated state. There are no global
    probabilities.
    
Assumptions made:
    1) RF Inhibit is always over.

@author: bdmolyne
"""


def deployment():
    '''All diamonds in deployment.
    
    Assuming SoC is above detumble threshold (wait otherwise)
    '''
    
    return {
        'eps_functionality' : 100,
        'tsp_functionality' : 100,
        'watchdog_functionality' : 100,
    
        'rw_functionality' : 100,
        'imu_functionality' : 100,
        'st_functionality' : 100,
        'ss_functionality' : 100,
    
        'recieved_non_standard_burn_wire_signal' : 100,
        
        'soc_above_burn_thresh' : 100,
        'charge_rate_positive' : 100
    }
    
    
def comms():
    '''All diamonds in Comms state.'''
    
    return {
        'tsp_functionality' : 100,
        'soc_above_radio_power_thresh' : 100,
        'is_radio_on' : 100,
        'radio_functionally_verified' : 100,
        'gnc_peripherials_on' : 100,
        
        'rw_functionality' : 100,
        'imu_functionality' : 100,
        'st_functionality' : 100,
        'ss_functionality' : 100,
        
        
    }
    


def warmup():
    '''All diamonds in Warmup state'''
    
    return {
        'eps_functionality' : 100,
        'tsp_functionality' : 100,
        'watchdog_functionality' : 100,
        
        'rw_functionality' : 100,
        'imu_functionality' : 100,
        'st_functionality' : 100,
        'ss_functionality' : 100,
        
        'any_rw_near_saturation' : 100,
        'is_rw_desaturation_state_in_stack' : 100,
        
        'enough_propelent_liquid' : 100,
        'soc_above_burn_threshold' : 30
    
    }
    
    
def predisposal():
    '''All diamonds in predisposal state'''
    
    return {
        'eps_functionality' : 100,
        'tsp_functionality' : 100,
        'watchdog_functionality' : 100,
        
        'rw_functionality' : 100,
        'imu_functionality' : 100,
        'st_functionality' : 100,
        'ss_functionality' : 100,
        
    }


def charge():
    '''All diamonds in charge state
    
    ASSUMPTION: Charge loop always succeeds'''
    
    return {
        'tsp_functionality' : 100,
        
        'gnc_peripherials_on' : 100,

        'rw_functionality' : 100,
        'imu_functionality' : 100,
        'st_functionality' : 100,
        'ss_functionality' : 100,
        
        'batteries_connected' : 100

    }
    

def burn():
    '''All diamonds in burn'''
    
    return {
        'tsp_functionality' : 100
        }

