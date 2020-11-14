#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 23:04:27 2020

@author: bdmolyne
"""

from logger import Logger
from database import Database
import config

logger = Logger() # instantiates logger object.
info = config.pack()
db = Database(info['phm'], info['hardware'], info['states']) # Instantiate component objects inside database.

# understand and clean up below 2 lines.
current_state_itr = info['states'].start_state
info['states'].current_state = info['states'].start_state

while current_state_itr != None:
    
    current_state = info['states'][current_state_itr]
    current_state.set_logger(logger)
    current_state.set_database(db)
    current_state.run_process()
    logger = current_state.get_logger() # retrieves the logger from the state.
    db = current_state.get_database() # retrieves the database from the state.
    
    current_state_itr = None # guarentees termination of simulation

logger.export() # exports the logger.