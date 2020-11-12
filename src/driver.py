#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 23:04:27 2020

@author: bdmolyne
"""

from logger import Logger
import config


logger = Logger() # instantiates logger object.
info = config.pack()

# understand and clean up below 2 lines.
current_state_itr = info['states'].start_state
info['states'].current_state = info['states'].start_state

while current_state_itr != None:
    
    current_state = info['states'][current_state_itr]
    current_state.set_logger(logger)
    current_state.run_process()
    logger = current_state.get_logger() # retrieves the logger from the state.
    
    current_state_itr = None

for log in logger:
    print(log.string)