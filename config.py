#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:18:07 2020

CONFIGURATION FILE FOR THE SIMULATION

"""

# Any necessary imports
from hardware import Hardware

# === GENERAL CONFIGURATION ===

# ==== END GENERAL CONFIG ====


# === HARDWARE CONFIGURATION ===

hardware = Hardware()

# Add in hardware to the simulation by doing hardware.add('name_of_hardware')
hardware.add('ReactionWheelX')
hardware.add('ReactionWheelY')
hardware.add('ReactionWheelZ', ma_dict = {'short' : 'RWz'})
hardware.add('IMU')

# ==== END HARDWARE CONFIG ====
