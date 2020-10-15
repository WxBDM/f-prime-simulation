#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:07:26 2020

@author: bdmolyne
"""


# Software States Simulation

# This script will simulate the various software states by generating random numbers
#   to determine what is happening in the satellite. Assume no corruption
#   has occured to the data due to radiation.


class StateStack:
    '''Represents the stack that is implemented in the software states.'''
    
    states = ['Warmup', 'Burn', 'Comms', 'Deployment', 'Contingency', 'Science', 'Charge', 
         'Pre-disposal', 'Disposal', 'Safety 1', 'Safety 2', "RW Desaturation"]
    

    def __init__(self):
        self._stack = []
    
    def __len__(self):
        '''Returns a length representation of the stack'''
        return len(self._stack)
    
    def __str__(self):
        '''Defines string representation of stack'''
        
        if len(self._stack) == 0:
            return "Stack is empty.\n"
        
        stack_str = "Stack bottom -> "
        for index, state in enumerate(self._stack):
            stack_str += state + " -> "
        stack_str += "top\n"
        
        return stack_str
    
    def to_string(self):
        '''If a string is needed (redundancy for __str__()'''
        return self.__str__()
    
    def get_top(self):
        '''Returns the top of the stack'''
        return self._stack[-1]

    def add_to_state_stack(self, l, indent = 0):
        '''Adds multiple to the stack, for USER purposes.'''
        
        if not isinstance(l, str) and not isinstance(l, list):
            raise ValueError("Must be list or str. Found: {}".format(type(l)))
       
        print("\tStack before: {}".format(self.to_string()))
        
        if isinstance(l, str):
           self.push(l, indent = indent)
        else:
            for state in l:
                self.push(state, indent = indent)
        
        print("\t" + self.to_string())

    def push(self, state, verbose = False, indent = 0):
        '''Adds a state to stack. Includes data checks.
        
        Arg: state (str) => The state name to add.'''
        
        # check to make sure it is a string (dev check)
        if not isinstance(state, str):
            raise ValueError('{} not type string. Found: {}'.format(state, type(state)))
        
        # check to make sure the state is in the possible states (dev check)
        if state not in self.states:
            raise ValueError("{} not in defined states.".format(state))
            return
        
        # find number of indents
        n_indents = ''
        for i in range(indent): n_indents += "\t"
            
        # apennd
        self._stack.append(state)
        print("{}{} added to state stack.".format(n_indents, state))
        if verbose: print(n_indents + self.__str__())
    
    def pop(self, verbose_pop = True, verbose = False, indent = 0):
        '''Removes the top-most state from the stack.
        
        Arg: None'''
        
        # find number of indents
        n_indents = ''
        for i in range(indent): n_indents += "\t"
        
        which_state = self._stack[-1]
        self._stack.pop(-1)
        if verbose_pop: print("{}{} removed from state stack.".format(n_indents, which_state))
        if verbose: print(n_indents + self.__str__())
        return which_state
        