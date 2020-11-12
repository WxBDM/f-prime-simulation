#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:18:07 2020

CONFIGURATION FILE FOR THE SIMULATION

"""

# Any necessary imports
from hardware_mgr import Hardware
from states_mgr import States
from phm_mgr import PHM

# This is the configuration file for the simulation. Register the hardware,
#   states, and phm

# === GENERAL CONFIGURATION ===
start_state = 'deployment'

# === END GENERAL CONFIG ===

# === HARDWARE CONFIGURATION ===

hardware = Hardware()

# Add in hardware to the simulation by doing hardware.register('name_of_hardware')
hardware.register('IMU')  
hardware.register('Computer')  
hardware.register('ReactionWheelX', {'sat_lim' : 0.075, 'is_on' : True})  

# ==== END HARDWARE CONFIG ====


# # === STATE CONFIGURATION ===

states = States()
states.start_state = 'charge' # <-- Change this to the state you want to start in.

from states.charge import ChargeState
states.register('charge', ChargeState())

# # ==== END STATE CONFIG ====



# # === PHM CONFIGURATION ===

phm = PHM()

phm.register('thermal', (-10, 40))

# # ==== END PHM CONFIG ====

def pack():
    return {'phm' : phm, 'hardware' : hardware, 'states' : states}


# ===================================
# === Do not edit below this line ===
# ===    Below is driver code.    ===
# ===================================

# Instantiate logger
# Pack all of the components into the logger.
#   this should create 3 dataframes: phm













