# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:48:04 2018

@author: baman
"""

from stack_program import Stack

def paranthesis_chck(symbol_string):
    s = Stack()
    balanced = True
    index = 0 
    while(index < len(symbol_string) and balanced):
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.is_empty():
        print('Paranthesis matched')
    else:
        print s.items
        print('Paranthesis not Matched')
    