#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:07:35 2020

@author: bdmolyne
"""

import pandas as pd
from types import MethodType
from database import Database

class PHM(Database):
    
    '''Prognostic Health Managemet system. Provides the interface between
    the user and the database/inner-workings.'''
    
    _d = {} # dictionary to make this object indexable.
    
    def __str__(self): # string representation when print()
        return self.db_phm_df.to_string()
    
    def __repr__(self): # string representation of the object and where it's located.
        return '<{}.{} object located at {}>'.format(self.__class__.__module__, 
                                        self.__class__.__name__, hex(id(self)))

    def __len__(self):
        return len(self.db_phm_df)

    def __getitem__(self, index):
        
        if index not in self._d.keys():
            error_msg = "Be sure to check the configuration file."
            raise ValueError("{} not added. {}".format(index, error_msg))
        
        return self._d[index]
           
    def register(self, name, bounds, ma_dict = {}):
        '''Adds a new PHM threshold into the system.
        
        Parameters:
            Required:
                name (string) => the name of the piece of hardware.
                bounds (tuple) => The INCLUSIVE bounds for the PHM. 2 values, (lower, upper)
            
            Optional:
                ma_dict (dict) => A dictionary containing the methods and attributes
                the user wishes to include with the PHM value. The key is the name
                of the method/attribute, and the value is either the function/method
                or attribute value.
        '''
        
        # Data type checks!
        error_msg = "Be sure to check the configuration file."
        
        # check to make sure it isn't registered already.
        if name in self.db_phm_df['name'].to_list():
            raise ValueError("{} is already registered. {}".format(name, error_msg))
        
        # Ensures the name is a string.
        if not isinstance(name, str):
            raise ValueError("name must be string. Found: {}. {}".format(type(name), error_msg))
        
        # Ensures ma_dict is a dictionary.
        if not isinstance(ma_dict, dict):
            raise ValueError("ma_dict must be a dictionary. Found: {}. {}".format(type(ma_dict), error_msg))
        
        # Ensures bounds is a tuple.
        if not isinstance(bounds, tuple):
            raise ValueError("bounds must be tuple. Found: {}. {}".format(type(bounds), error_msg))
        
        # Ensures bounds tuple is length of 2.
        if len(bounds) != 2:
            raise ValueError("Bounds must be length 2. Found: {}. {}".format(len(bounds), error_msg))
        
        # Ensures that there's a number (or none type) associated with each bound.
        if not isinstance(bounds[0], (float, int, type(None))):
            raise ValueError("First bound invalid; must be int/float. Found: {}. \
                             {}".format(type(bounds[0]), error_msg))
        if not isinstance(bounds[1], (float, int, type(None))):
            raise ValueError("First bound invalid; must be int/float. Found: {}. \
                             {}".format(type(bounds[1]), error_msg))
        
        # Compare the two bounds unless it's a none type.
        if None not in bounds and bounds[0] > bounds[1]:
            raise ValueError("Lower bound greater than upper bound. {}".format(error_msg))
        
        # check to see if all of the values are none.
        if bounds[0] is None and bounds[1] is None:
            raise ValueError("Both bounds can not be None. {}".format(error_msg))
    
        # set the initial dictionary, and then update it with ma_dict
        data_d = {'name' : name, 'lower_bound' : bounds[0], 'upper_bound' : bounds[1]}
        data_d.update(ma_dict)
        
        # load it into a series, then into info.
        series = pd.Series(data = data_d)
        
        # add it to the object dictionary. This is used only for interfacing
        #   with the pandas dataframe.
        self._d[name] = self._to_object(name, series)
        self.db_phm_df = self.db_phm_df.append(series, ignore_index = True)
    
    def _to_object(self, name, series):
        """Gets the object representation of the PHM value."""

        attribute_d = {}
        columns = list(series.index) # get the column names
        for col_name in columns:
            attribute_d[col_name] = series.loc[col_name]
        attribute_d['_series'] = series # adding this to object so that it can be printed.
        
        # functions for new object.
        # thank you. https://www.ianlewis.org/en/dynamically-adding-method-classes-or-class-instanc
        
        def obj_check_thresh(self, n):
            '''Checks to see if the parameter has exceeded a value in the PHM.'''
            
            # dev checks
            # check to make sure it's an int or a float.
            if not isinstance(n, (int, float)):
                raise ValueError("Value not int/float. Found: {}".format(type(n)))
     
            # checks upper bound
            if not isinstance(self.upper_bound, type(None)):
                if self.upper_bound > n:
                    return True
            
            # checks lower bound
            if not isinstance(self.lower_bound, type(None)):
                if self.lower_bound < n:
                    return True
            
            # If it didn't exceed upper bound or lower bound, return False
            #   stating it is nominal.
            return False
        
        def obj_magic_str(self): return self._series.to_string()

        
        # add in the methods for the object.
        new_obj = type(name, (), attribute_d)
        new_obj.check_threshold = MethodType(obj_check_thresh, new_obj)
        new_obj.__str__ = MethodType(obj_magic_str, new_obj)
        inst_obj = new_obj() #instantiate it.
        return inst_obj
    
    

