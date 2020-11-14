#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from actions import Actions

class ChargeState():
    
    def set_logger(self, logger_obj):
        self.logger = logger_obj
    
    def set_database(self, db_obj):
        self._database = db_obj
    
    def get_logger(self):
        return self.logger
    
    def get_database(self):
        return self._database
    
    def reset_db_and_logger(self, actions_obj):
        self.logger = actions_obj.logger # gets the logger from the actions class.
        self.db = actions_obj.database
    
    def phm_values(self):
        
        d = {'rotation_x' : (None, 5), 
             'rotation_y' : (None, 5),
             'rotation_z' : (None, 5),
             'soc' : (16, None),
             'thermal' : (-10, 40),
              }
        
        return d

    def decision_probability(self):
        
        d = {'tsp_funct_verified' : 100,
             'peripheral_funct_verified' : 0
             }
    
        return d
        
    def run_process(self):
        '''Runs the charge state process.'''
        
        self._database.phm.register(self.phm_values())
        self.logger.set_state('charge')
        actions = Actions(self.logger, self._database) # instantiates action class, sets logger and db
        actions.probabilities = self.decision_probability()
        
        # ==== vvvv YOUR CODE GOES BELOW THIS vvv ====
        
        actions.database.components_to_series()
        
        actions.charge_run_init_program()
        tsp_set_correctly = actions.verify_tsp()
        if not tsp_set_correctly:
            actions.add_to_state_queue('charge')
            actions.add_to_state_queue('safety1')
            self.reset_db_and_logger()
            actions.check_stack()
            return
            
        # actions.set_phm_flags()
        # actions.read_optimal_charge_vector()
        # actions.turn_on_peripherals()
        # peripherals_ok = actions.check_peripherals()
        # if not peripherals_ok:
        #     actions.add_to_state_queue('charge')
        #     actions.add_to_state_queue('safety1')
        #     actions.check_stack()
        #     return
        
        # actions.acquire_sun_position()
        # actions.initiate_sun_pointing()
        # actions.charge()
        # actions.terminate_sun_pointing()
        # actions.check_stack()
    
        # ============================================

        self.reset_db_and_logger()

        return



