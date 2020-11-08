#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:01:12 2020

@author: bdmolyne
"""

import pandas as pd
from types import MethodType


class Hardware:
    
    '''The Hardware class defines all of the hardware that is on board of the satellite.
    Includes:
        IMU, EPS, OBC, ST, SS, Reaction Wheel (all 3 axis)
        
    Any values that are in here are specified by the hardware manufacturer.
    '''
            
    # ground breaking: https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
    
    _d = {} # dictionary to make this object indexable.
    
    def __init__(self): # initialization
        # save it into a dataframe.
        self.info = pd.DataFrame(columns = ['name', 'is_on'])
    
    def __getitem__(self, index):
        return self._d[index]
    
    def add(self, name, ma_dict = {}):
        '''Adds a new piece of hardware to the system. This dynamically generates
        a hardware object and adds it to the hardware class.
        
        Parameters:
            Required:
                name (string) => the name of the piece of hardware.
            
            Optional:
                ma_dict (dict) => A dictionary containing the methods and attributes
                the user wishes to include with the hardware. The key is the name
                of the method/attribute, and the value is either the function/method
                or attribute value.
        
        Note that this assumes that the hardware is off.
        '''
        
        # user checks, ensures data type is correct.
        if not isinstance(name, str):
            error_msg = "Be sure to check the configuration file."
            raise ValueError("name must be string. Found: {}. {}".format(type(name), error_msg))
        
        if not isinstance(ma_dict, dict):
            raise ValueError("ma_dict must be a dictionary. Found: {}")
            
        # check to make sure that the piece of hardware is not already in the dataframe
        if name in self.info['name'].to_list():
            raise ValueError("{} is already in dataframe.".format(name))
        
        # set the initial dicitonary, and then update it with ma_dict
        data_d = {'name' : name, 'is_on' : False}
        data_d.update(ma_dict)
        
        # load it into a series, then into info.
        to_load = pd.Series(data = data_d)
        self.info = self.info.append(to_load, ignore_index = True)
        
        # add it to the object dictionary. This is used only for interfacing
        #   with the pandas dataframe.
        self._d[name] = self.to_object(name)
        
    
    def __str__(self): # string representation when print()
        return self.info.to_string()
    
    def __repr__(self): # string representation of the object and where it's located.
        return '<{}.{} object located at {}>'.format(self.__class__.__module__, 
                                        self.__class__.__name__, hex(id(self)))
    
    def to_object(self, name):
        """Gets the object representation of the hardware."""
        
        if not isinstance(name, str):
            raise ValueError("Name parameter must be string. Found: {}.".format(type(name)))
        
        if name not in self.info['name'].to_list():
            raise ValueError("{} is not found in hardware dataframe.".format(name))
        
        # determines if the hardware is on or off.
        row = self.info.loc[self.info['name'] == name]
        
        attribute_d = {}
        for col_name in row.iloc[0].index.to_list():
            attribute_d[col_name] = row.iloc[0][col_name]
        
        # functions for new object.
        # thank you. https://www.ianlewis.org/en/dynamically-adding-method-classes-or-class-instanc
        def turn_off(self): self.is_on = False
        def turn_on(self): self.is_on = True
        
        # add in the methods for the object.
        new_obj = type(name, (), attribute_d)
        new_obj.turn_on = MethodType(turn_on, new_obj)
        new_obj.turn_off = MethodType(turn_off, new_obj)
        return new_obj





