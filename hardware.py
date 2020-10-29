#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:01:12 2020

@author: bdmolyne
"""

import pandas as pd

class Hardware:
    
    '''The Hardware class defines all of the hardware that is on board of the satellite.
    Includes:
        IMU, EPS, OBC, ST, SS, Reaction Wheel (all 3 axis)
        
    Any values that are in here are specified by the hardware manufacturer.
    '''
    
    class Methods:
        
        def __init__(self):
            self.is_on = False
        
        def convert_bool(self, val):
            if not isinstance(val, bool):
                raise ValueError("val is not bool. Found: {}".format(type(val)))
            
            if val: return 1
            return 0
        
        def turn_on(self):
            self.is_on = True
        
        def turn_off(self):
            self.is_on = False
    
    class ReactionWheelX(Methods):
        
        def __init__(self):
            super().__init__()
            self.is_on = True
        
        def saturation_limit(self):
            return 0.075
        
        @staticmethod
        def str_repr():
            return "RWx"
    
    class ReactionWheelY(Methods):
        
        def __init__(self):
            super().__init__()
            self.is_on = True
        
        def saturation_limit(self):
            return 0.0375
        
        @staticmethod
        def str_repr():
            return "RWy"
    
    class ReactionWheelZ(Methods):
        
        def __init__(self):
            super().__init__()
            self.is_on = True
        
        def saturation_limit(self):
            return 0.075
        
        @staticmethod
        def str_repr():
            return "RWz"
    
    class SunSensor(Methods):
        
        def __init__(self):
            super().__init__()
        
        @staticmethod
        def str_repr():
            return "SS"
    
    class StarTracker(Methods):
        
        def __init__(self):
            super().__init__()
       
        @staticmethod
        def str_repr():
            return "ST"
        
    class InertialMeasurementUnit(Methods):
        
        def __init__(self):
            super().__init__()
            
        @staticmethod
        def str_repr():
            return "IMU"
    
    class ElectricalPowerSystem(Methods):
       
        def __init__(self):
            super().__init__()
        
        @staticmethod
        def str_repr():
            return "EPS"
    
    class OnboardComputer(Methods):
        
        def __init__(self):
            super().__init__()
        
        @staticmethod
        def str_repr():
            return "OBC"
    
    class Radio(Methods):
        
        def __init__(self):
            super().__init__()
        
        @staticmethod
        def str_repr():
            return "Radio"
        
    
    def __init__(self): # initialization
        '''Constructor for Hardware class. Initalizes all instances of hardware objects.'''

        # Dynamically generate this, this is short term and not hard coded, as we may add
        # in new hardware at a later time or need to reorganize it.
        
        self.rw_x = self.ReactionWheelX()
        self.rw_y = self.ReactionWheelY()
        self.rw_z = self.ReactionWheelZ()
        self.ss = self.SunSensor()
        self.st = self.StarTracker()
        self.imu = self.InertialMeasurementUnit()
        self.eps = self.ElectricalPowerSystem()
        self.obc = self.OnboardComputer()
        
        # Will need these for turning on peripherals.
        self.peripherals = [self.ss, self.st, self.imu, self.rw_x, self.rw_y, self.rw_z]
        
        hardware_list = [self.rw_x, self.rw_y, self.rw_z, self.ss, self.st, self.imu, 
                        self.eps, self.obc]
        
        # string representation of hardware (abbreviation)
        name = [x.str_repr() for x in hardware_list]
        
        # if it's on (true = on, false = off)
        hardware_power = [x.is_on for x in hardware_list]
        
        # binary version of above (0 off, 1 on)
        hardware_binary = [x.convert_bool(x.is_on) for x in hardware_list]
        
        # compile data into dictionary, prep for dataframe
        data = {'name' : name, 'is_on' : hardware_power, 'is_on_binary' : hardware_binary}
        
        # save it into a dataframe.
        self.info = pd.DataFrame(data = data)
    
    def __str__(self): # string representation when print()
        return self.info.to_string()
    
    def __repr__(self): # string representation of the object and where it's located.
        return '<{}.{} object located at {}>'.format(self.__class__.__module__, 
                                        self.__class__.__name__, hex(id(self)))

    def gnc_peripherals_on(self):
        
        '''Determines if any of the GNC peripherals are on. 
        
        If all are on, return True. Otherwise, False'''
        
        periph = [self.ss.is_on, self.st.is_on, self.imu.is_on, self.rw_x.is_on,
                  self.rw_y.is_on, self.rw_z.is_on]
        
        return all(periph)

    def turn_on_gnc_periph(self):
        '''Turns on all of the peripherals. Note that this is condensed into one
        block, and not individually.'''
        
        for periph in self.peripherals:
            periph.turn_on()

