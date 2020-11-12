#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:01:12 2020

@author: bdmolyne
"""

import pandas as pd
from types import MethodType

class Hardware():
    
    '''The Hardware class defines all of the hardware that is on board of the satellite.
    '''
            
    # ground breaking: https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
    
    db_hardware_df = pd.DataFrame(columns = ['name', 'is_on'])
    _d = {} # dictionary to make this object indexable.
    
    def __getitem__(self, index):
        
        if index not in self._d.keys():
            error_msg = "Be sure to check the configuration file."
            raise ValueError("{} not added. {}".format(index, error_msg))
        
        return self._d[index]

    def __str__(self): # string representation when print()
        return self.db_hardware_df.to_string()
    
    def __repr__(self): # string representation of the object and where it's located.
        return '<{}.{} object located at {}>'.format(self.__class__.__module__, 
                                        self.__class__.__name__, hex(id(self)))
    
    def __len__(self):
        return len(self.db_hardware_df)
    
    def register(self, name, ma_dict = {}):
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
        if name in self.db_hardware_df['name'].to_list():
            raise ValueError("{} is already in dataframe.".format(name))
        
        # set the initial dictionary, and then update it with ma_dict
        data_d = {'name' : name, 'is_on' : False}
        data_d.update(ma_dict)
        
        # load it into a series, then into info.
        series = pd.Series(data = data_d)
        
        # add it to the object dictionary. This is used only for interfacing
        #   with the pandas dataframe.
        self._d[name] = self._to_object(name, series)
        self.db_hardware_df = self.db_hardware_df.append(series, ignore_index = True)
    
    def _to_object(self, name, series):
        """Gets the object representation of the hardware."""
        
        attribute_d = {}
        columns = list(series.index) # get the column names
        for col_name in columns:
            attribute_d[col_name] = series.loc[col_name]
        attribute_d['_series'] = series # adding this to object so that it can be printed.
        
        # functions for new object.
        # thank you. https://www.ianlewis.org/en/dynamically-adding-method-classes-or-class-instanc
        def turn_off(self): self.is_on = False
        def turn_on(self): self.is_on = True
        def obj_magic_str(self): return self._series.to_string()
        
        # add in the methods for the object.
        new_obj = type(name, (), attribute_d)
        
        # add the methods above.
        new_obj.turn_on = MethodType(turn_on, new_obj)
        new_obj.turn_off = MethodType(turn_off, new_obj)
        new_obj.__str__ = MethodType(obj_magic_str, new_obj)
        
        inst_obj = new_obj() #instantiate it.
        return inst_obj





