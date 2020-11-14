#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:14:37 2020

@author: bdmolyne

"""

import pandas as pd

class Logger:
    
    logger_node_df_list = []
    _node_id = 0
    
    class LoggerNode:
        
        def __init__(self, node_id):
            self._id = node_id
            self.string = None
        
        def __str__(self):
            logger_str = 'Logger node {}: string: {}'.format(self._id, self.string)
            return logger_str
        
        def add_string(self, string):
            if not isinstance(string, str):
                raise ValueError("string")
            self.string = string
        
        def to_series(self, state):
            s_data = {'id' : self._id, 'state' : state, 'string' : self.string}
            series = pd.Series(data = s_data)
            return series
                
    def __len__(self):
        return len(self.logger_node_list)

    def __str__(self):
        return str(self.logger_node_list)

    def __getitem__(self, index):
        return self.logger_node_list[index]

    def set_state(self, state_str):
        # dtype check needed
        self.state = state_str
    
    def add(self, logger_node, database_obj):
        
        if not isinstance(logger_node, self.LoggerNode):
            raise ValueError("Did not recieve logger node object. Recieved: {}".format(type(logger_node))) 
        
        # find a way to check to see if it's the database object.
        # if not isinstance(database_obj, database.Database):
        #     raise ValueError("Did not recieve database object. Recieved: {}".format(type(database_obj))) 

        series = database_obj.components_to_series() # put the components into a series
        series = series.sort_index()
        full_node = logger_node.to_series(self.state).append(series)
        self.logger_node_df_list.append(full_node)
    
    def create_node(self):
        node = self.LoggerNode(self._node_id)
        self._node_id += 1
        return node
    
    def export(self, path = None):
        df = pd.DataFrame({})
        for node in self.logger_node_df_list:
            df = df.append(node, ignore_index = True)
        
        # for some reason it comes out alphabetized. This puts it in
        #   [id, state, string, rest in alphabet order]
        ordered_cols = ['id', 'state', 'string']
        ordered_cols_dynamic = [x for x in df.columns if x not in ordered_cols]
        all_cols = ordered_cols + ordered_cols_dynamic
        df = df[all_cols]
        
        # export it
        if path is None:
            path = ""
            
        df.to_csv("{}test.csv".format(path), index = False)

