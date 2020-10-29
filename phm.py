#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:07:35 2020

@author: bdmolyne
"""

import pandas as pd

class PHM:
    '''Prognostic Health Managemet system. The PHM flags are represented
    as a pandas dataframe.
    
    Example PHM (stored in memory):
              soc  thremal  rotation_x  ...  rw_sat_x  rw_sat_y  rw_sat_z
lower_bound  16.0      -10         NaN  ...       NaN       NaN       NaN
upper_bound   NaN       40         5.0  ...     0.075    0.0375     0.075

    When printed (i.e. print(PHM())), it will display the transposed:
        
                    lower_bound  upper_bound
        rotation_x          NaN       5.0000
        rotation_y          NaN       5.0000
        rotation_z          NaN       5.0000
        rw_sat_x            NaN       0.0750
        rw_sat_y            NaN       0.0375
        rw_sat_z            NaN       0.0750
        soc                16.0          NaN
        thremal           -10.0      40.0000
    
    When instantiating a new PHM object (should only be done once), it will
        instantiate an empty pandas dataframe.
    '''
    
    def __init__(self):
        self.flags = pd.DataFrame({})
        self.is_empty = True
    
    def __str__(self):
        
        df = self.flags
        df = df.rename({0: 'lower_bound', 1: 'upper_bound'}, axis='index')
        df = df.reindex(sorted(df.columns), axis=1)
        df = df.transpose()
        return df.to_string()

    def __len__(self):
        
        # transposing it will show us how many PHM values there are. Otherwise,
        #   it will always be 2.
        return len(self.flags.transpose())

    def get_flags(self):
        '''Returns a list of flags.'''
        
        return list(self.flags.columns)
        
    def set_flags(self, d):
        '''Sets the PHM flags in pandas DataFrame. The dictionary should be structured as such:
            
            {
             'phm_value_1' : (lower_bound_1, upper_bound_1),
             'phm_value_2' : (lower_bound_2, upper_bound_2),
             ...
             'phm_value_n' : (lower_bound_n, upper_bound_n)
            }
            
            Note the following format of the dictionary:
                key data type = string
                value data type = tuple
                    - Data types of tuple is either string, float, or None
                value length = 2
            
             - If the PHM value does not have a lower or upper bound, simply put type None.
             - Units of the bounds are NOT accounted for.
            
            === EXAMPLE VALID DICTIONARY FORMAT ===

                {
                 'soc' : (16, None),
                 'thermal' : (-10, 40),
                 'rotation_x' : (None, 5)
                }
            
            =======================================
            
            Translation to English:
                'soc' : (16, None) => "The state of charge has a lower bound of 16 W-hr with no upper bound."
                'thermal' : (-10, 40) => "The temprature can not go lower than -10C and can not go higher than 40C"
                'rotation_x' : (None, 5) =>"The rotation of the satellite has no
                    lower bound, but has an upper bound of 5 deg/sec"
         '''
        
        def error_here_str(key, value):
            '''Refactored string, to be used only in set_flags()'''
            return "Error here => {} : {}".format(key, value)

        # data type checks!
        # make sure it is a dictionary
        if not isinstance(d, dict):
            raise ValueError("Flags not in data structure of dictionary, found {}".format(type(d)))
        
        if len(d) == 0:
            raise ValueError("Flags should not be empty. Go back into `phm_flags` method" \
                             " and double check to ensure this dicitonary is not empty.")
        if len(d) == 1:
            # if it's the driver code or a state.
            if d['state'] == 'PHM_DRIVER_CODE':
                origin = 'driver code dictionary (at bottom of phm.py)'
            else:
                origin = '{} `phm_flags` method'.format(d['state'])
            
            raise ValueError("Flags should not be empty. Go back into {}" \
                             " and double check to ensure flags are set. Refer to doc string" \
                             " for formatting help.".format(origin))
        
        # make sure each value in the dictionary is a tuple.
        # furthermore, check value to make sure it's either None or an int/float.
        # check to make sure there's only 2 values in tuple!
        # furthermore, check key to make sure it's a string.
        for phm_dict_key in d:
            
            if phm_dict_key == 'state': continue
            
            phm_dict_val = d[phm_dict_key]
            
            # check to make sure that it's a string
            if not isinstance(phm_dict_key, str):
                error_msg = "Key not string. Found: {}\n{}".format(type(phm_dict_key),
                                                    error_here_str(phm_dict_key, phm_dict_val))
                raise ValueError(error_msg)
            
            # check to make sure the value is a tuple
            if not isinstance(phm_dict_val, tuple):
                error_msg = "Value not tuple. Found: {}\n{}".format(type(phm_dict_val), 
                                                    error_here_str(phm_dict_key, phm_dict_val))
                raise ValueError(error_msg)
                
            # check tuple length.
            if len(phm_dict_val) != 2:
                error_msg = "Value is not length 2. Actual length: {}\n{}".format(len(phm_dict_val), 
                                                    error_here_str(phm_dict_key, phm_dict_val))
        
            # iterate through tuple.
            for tuple_value in phm_dict_val:
                if not any([isinstance(tuple_value, int), isinstance(tuple_value, float), 
                            isinstance(tuple_value, type(None))]):
                    error_msg = "Value tuple not int, float, or None. Found: {}\n{}".format(type(tuple_value), 
                                                    error_here_str(phm_dict_key, phm_dict_val))
                    raise ValueError(error_msg)
                
        
        # If the code gets here, the dictionary is properly formatted.
        # Put into pandas dataframe.
        df = pd.DataFrame(d)
        self.flags = df.rename({0: 'lower_bound', 1: 'upper_bound'}, axis='index')
        
        # sets 
        if len(self.flags) != 0:
            self.is_empty = False
        else:
            self.is_empty = True
        
        # TODO: Add to PHM event logger.
    
    def check_exceedence(self, param, thresh):
        '''Checks to see if the parameter has exceeded a value'''
        
        # dev checks
        # check to make sure the parameter that's being passed in is 
        if not isinstance(param, str):
            raise ValueError("Parameter not a string. Found: value: {}, int: {}".format(param, type(param)))
        
        # if the parameter is not in the phm flags dictionary, throw an error.
        if param not in self.flags:
            raise ValueError("{} not found in flag dataframe.\nCurrent flags: {}".format(param, 
                                                        list(self.flags.keys())))
        
        # check to make sure it's an int or a float.
        if not isinstance(thresh, int) and not isinstance(thresh, float):
            raise ValueError("Value not int/float. Found: {}".format(type(thresh)))
        
        upper_bound_thresh = self.flags[param][0]
        lower_bound_thresh = self.flags[param][1]
        
        # O(1)
        # checks upper bound
        if not isinstance(upper_bound_thresh, type(None)):
            if upper_bound_thresh > thresh:
                return (True, 1, param)
        
        # checks lower bound
        if not isinstance(lower_bound_thresh, type(None)):
            if lower_bound_thresh < thresh:
                return (True, 0, param)
        
        # If it didn't exceed upper bound or lower bound, return False
        #   stating it is nominal.
        return False
            
        
        
        
        
# DRIVER CODE   
sample_phm_dict = {'state' : 'PHM_DRIVER_CODE',
                    'soc' : (16, None),
                    'thremal' : (-10, 40),
                    'rotation_x' : (None, 5),
                    'rotation_y' : (None, 5),
                    'rotation_z' : (None, 5),
                    'rw_sat_x' : (None, 0.075),
                    'rw_sat_y' : (None, 0.0375),
                    'rw_sat_z' : (None, 0.075)
                   }

phm = PHM() # <-- This object will be passed around in driver dictionary.
phm.set_flags(sample_phm_dict)

ex = phm.check_exceedence('soc', 10)
if ex[0]:
    if ex[1] == 0:
        print("PHM upper bound exceeded!")
    if ex[1] == 1:
        print("PHM lower bound exceeded!")
# ====















