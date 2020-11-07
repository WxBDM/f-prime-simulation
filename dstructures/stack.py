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

# How the stack is implemented:
    # FILO structure
    # List implementation. Last element in list is the one to pop/push.

class StateStack:
    '''Represents the stack that is implemented in the software states'''
    
    state_map = {'Burn': 1, 'Charge' : 2, 'Comms' : 3, 'Contingency' : 4,
                 'Deployment' : 5, 'Disposal' : 6, 'Pre-disposal' : 7, 
                 'RW Desaturation' : 8, 'Safety 1' : 9, 'Safety 2' : 10,
                 'Science' : 11, 'Warmup' : 12}
    
    states = ['Warmup', 'Burn', 'Comms', 'Deployment', 'Contingency', 'Science', 'Charge', 
         'Pre-disposal', 'Disposal', 'Safety 1', 'Safety 2', "RW Desaturation"]
    
    # Magic methods - no need to edit.
    # ======
    def __init__(self): # initialization
        '''Constructor for Stack class. List-based stack.'''
        
        self._stack = []
        self._top_val = None
    
    def __len__(self): # length of stack
        '''Returns the length of the stack'''
        
        return len(self._stack)
    
    def __getitem__(self, position): # here for iteration purposes (seeing what's in the stack)
        return self._stack[position]

    def __str__(self): # string representation when print()
        
        if self.__len__() == 0:
            return "Empty stack\n"
    
        stack_str = "["
        for index, val in enumerate(self._stack):
            if index == 0:
                stack_str += "{}".format(val)
            else:
                stack_str += ", {}".format(val)
        
        return stack_str
    
    def __repr__(self): # string representation of the object and where it's located.
        return '<{}.{} object located at {}>'.format(self.__class__.__module__, 
                                        self.__class__.__name__, hex(id(self)))
    
    def __eq__(self, other): # determining if 2 stacks are equal
        if not isinstance(other, StateStack):
            raise ValueError("{} is not StateStackRewrite. Type found: {}".format(other, type(other)))
    
        for index, other_ele in enumerate(other):
            if self._stack[index] != other_ele:
                return False
        
        return True
    # ========


    # Behavior methods
    # =========
    def _generateVerboseStr(self, string, n_indents):
        '''Generate the string to be printed to console when you push/pop.
        
        ** DEV TOOL: refactor **
        
        Arguments:
            string (str) (required) => The string to print out.
            n_indents (int) (required) => the number of indents for the string.
        
        Returns:
            verbose_str (str) => the string to print to console.
        
        Sample returns:
            \t\tState 1 added to Stack.
            Current stack: [1, 3, 1
            
            State 3 removed from stack.
            Current stack: [5, 2
        
        '''
        
        # dev test
        if not isinstance(n_indents, int):
            raise ValueError("n_indents must be an int. Got type: {}".format(type(n_indents)))
        if not isinstance(string, str):
            raise ValueError("string must be a str. Got type: {}".format(type(n_indents)))
        
        verbose_str = ""
        for n_indents in range(n_indents):
            verbose_str += "\t"
        
        verbose_str += "{}\n".format(string)
        verbose_str += "Current stack: {}".format(self.__str__())
        
        return verbose_str
        
    def to_string(self):
        return self.__str__()
    
    def push(self, val, verbose = False, verbose_indent = 0):
        '''Add a value to the stack.
        
        Arguments:
            val (required) (list, tuple, or string) => the value to add to the stack
            verbose (optional) => print out operation and what the stack looks like after addition.
            verbose_indent (optional) => UI purposes, how many indents the text should be.
        
        Returns:
            None
        '''
        
        # Check to see if it's a list/tuple or individual item.
    
        # if it's a list, literate through and append.
        if isinstance(val, list) or isinstance(val, tuple):
            for element in val:
                self._stack.append(val)
                if verbose:
                    verbose_str = self._generateVerboseStr(
                        "{} added to stack.".format(val), verbose_indent)
                    print(verbose_str)
                    
        # For now, check strings. Could eventually map a number to associated state.
        elif isinstance(val, str):
            self._stack.append(val)
            if verbose:
                verbose_str = self._generateVerboseStr(
                    "{} added to stack.".format(val), verbose_indent)
                print(verbose_str)
        # if it's not list, tuple, or string then raise an error (dev check)
        else:
            raise ValueError("Must be either list, tuple, or string.")
        
    
    def pop(self, verbose = False, verbose_indent = 0):
        '''Remove a value from the stack.
        
        Arguments: None
        
        Returns: The value that was removed.'''
        
        # If there is nothing on the stack, print an error warning and stop method.
        if len(self.__stack) == 0:
            print("Unable to remove value from stack; stack is empty.")
            return None
        
        # The stack has a value; remove, print information, return value.
        return_val = self._stack[-1]
        self._stack.pop(-1)
        
        # print out information with the stack if verbose.
        if verbose:
            if len(self._stack) == 0:
                verbose_str = self._generateVerboseStr("Stack is empty.", verbose_indent)
            
            else:   
                verbose_str = self._generateVerboseStr("{} removed from stack.".format(return_val), verbose_indent)
        
            print(verbose_str)
        
        
        return return_val
    
    # =========