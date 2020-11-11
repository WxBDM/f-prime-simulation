#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:18:07 2020

CONFIGURATION FILE FOR THE SIMULATION

"""

# Any necessary imports
from hardware import Hardware
# from states import States
from phm import PHM

# This is the configuration file for the simulation. Register the hardware,
#   states, and phm

# === GENERAL CONFIGURATION ===
start_state = 'deployment'

# === END GENERAL CONFIG ===

# === HARDWARE CONFIGURATION ===

hardware = Hardware()

# Add in hardware to the simulation by doing hardware.add('name_of_hardware')
hardware.register('IMU')  
hardware.register('Computer')  
hardware.register('ReactionWheelX', {'sat_lim' : 0.075, 'is_on' : True})  

# ==== END HARDWARE CONFIG ====


# # === STATE CONFIGURATION ===
# state = States()

# state.register('deployment')

# state.start_state = None # <-- Change this to the state you want to start in.

# # ==== END STATE CONFIG ====



# # === PHM CONFIGURATION ===
phm = PHM()

phm.register('thermal', (-10, 40))

# # ==== END PHM CONFIG ====




# ===================================
# === Do not edit below this line ===
# ===    Below is driver code.    ===
# ===================================

# Instantiate logger
# Pack all of the components into the logger.
#   this should create 3 dataframes: phm












