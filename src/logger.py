#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:14:37 2020

@author: bdmolyne

"""

class Logger:
    
    logger_node_list = []
    _node_id = 0
    
    class LoggerNode:
        
        def __init__(self, node_id):
            self._id = node_id
        
        def __str__(self):
            return self.string
        
        def add_string(self, string):
            if not isinstance(string, str):
                raise ValueError("string")
            self.string = string
                
    def __len__(self):
        return len(self.logger_node_list)

    def __str__(self):
        return str(self.logger_node_list)

    def __getitem__(self, index):
        
        return self.logger_node_list[index]
    
    def create_new_event(self):
        '''Logger method to a new EVENT node'''
        return self.Event()
    
    def add(self, logger_node):
        
        if not isinstance(logger_node, self.LoggerNode):
            raise ValueError("Logger node.")
        
        self.logger_node_list.append(logger_node)
    
    def create_node(self):
        node = self.LoggerNode(self._node_id)
        self._node_id += 1
        return node

