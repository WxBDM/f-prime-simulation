#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 09:00:33 2020

Testing code for the logger. The logger follows TTD cycle.

@author: bdmolyne
"""

from logger import Logger
import unittest

class TestClass(unittest.TestCase):
    
    def setUp(self):
        self.logger = Logger()
    
    def test_3_dataframes_exist(self):
        '''Tests to ensure that there are 3 dataframes'''
        self.logger.phm
        self.logger.hardware
        self.logger.events
    
    def test_successful_add_to_df_all(self):
        pass

    def test_add_to_phm_are_all_df_same_size(self):
        
        d = {1 : 2, 3 : 4}
        self.logger.add_to_phm(d)
        
        msg1 = "phm length not equal to events. PHM: {}, events: {}".format(
                            len(self.logger.phm), len(self.logger.events))
        self.assertEqual(len(self.logger.phm), len(self.logger.events), msg1)
        
        msg2 = "phm length not equal to hardware. PHM: {}, hardware: {}".format(
                            len(self.logger.phm), len(self.logger.hardware))
        self.assertEqual(len(self.logger.phm), len(self.logger.hardware), msg2)

    def test_add_to_events_are_all_df_same_size(self):
        
        d = {1 : 2, 3 : 4}
        self.logger.add_to_events(d)
        
        msg1 = "events length not equal to phm. events: {}, phm: {}".format(
                            len(self.logger.events), len(self.logger.phm))
        self.assertEqual(len(self.logger.phm), len(self.logger.events), msg1)
        
        msg2 = "events length not equal to hardware. events: {}, hardware: {}".format(
                            len(self.logger.events), len(self.logger.hardware))
        self.assertEqual(len(self.logger.events), len(self.logger.hardware), msg2)
    
    def test_add_to_hardware_are_all_df_same_size(self):
        
        d = {1 : 2, 3 : 4}
        self.logger.add_to_hardware(d)
        
        msg1 = "hardware length not equal to phm. hardware: {}, phm: {}".format(
                            len(self.logger.hardware), len(self.logger.phm))
        self.assertEqual(len(self.logger.phm), len(self.logger.hardware), msg1)
        
        msg2 = "hardware length not equal to events. hardware: {}, events: {}".format(
                            len(self.logger.hardware), len(self.logger.events))
        self.assertEqual(len(self.logger.events), len(self.logger.hardware), msg2)
    
    
    def tearDown(self):
        self.logger = Logger()

if __name__ == "__main__":
    unittest.main()
    
    
    






