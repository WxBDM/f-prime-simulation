#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:01:12 2020

@author: bdmolyne
"""

import pandas as pd

class States():
    
    '''The states interface class to communicate with the PHM and the database.
    '''
            
    # ground breaking: https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
    
    _d = {} # dictionary to make this object indexable.
    db = pd.DataFrame(columns = ['name'])
    mgr_type = 'states'
    
    def __init__(self): # initialization
        pass
    
    def __getitem__(self, index):
        
        if index not in self._d.keys():
            error_msg = "Be sure to check the configuration file."
            raise ValueError("{} not added. {}".format(index, error_msg))
        
        return self._d[index]

    def __str__(self): # string representation when print()
        return self.db.to_string()
    
    def __repr__(self): # string representation of the object and where it's located.
        return '<{}.{} object located at {}>'.format(self.__class__.__module__, 
                                        self.__class__.__name__, hex(id(self)))
    
    def register(self, name, obj, ma_dict = {}):
        '''Registers a new state to the system. This dynamically generates
        a hardware object and adds it to the hardware class.
        
        Parameters:
            Required:
                name (string) => the name of the piece of hardware.
            
            Optional:
                ma_dict (dict) => A dictionary containing the methods and attributes
                the user wishes to include with the state. The key is the name
                of the method/attribute, and the value is either the function/method
                or attribute value.
        '''
        
        # user checks, ensures data type is correct.
        if not isinstance(name, str):
            error_msg = "Be sure to check the configuration file."
            raise ValueError("name must be string. Found: {}. {}".format(type(name), error_msg))
        
        if not isinstance(ma_dict, dict):
            raise ValueError("ma_dict must be a dictionary. Found: {}")
            
        # check to make sure that the piece of hardware is not already in the dataframe
        if name in self.db['name'].to_list():
            raise ValueError("{} is already in dataframe.".format(name))
        
        # set the initial dictionary, and then update it with ma_dict
        data_d = {'name' : name}
        data_d.update(ma_dict)
        
        # load it into a series, then into info.
        series = pd.Series(data = data_d)
        self.db = self.db.append(series, ignore_index = True)
        
        # add it to the object dictionary. This is used only for interfacing
        #   with the pandas dataframe.
        self._d[name] = obj




