# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:28:40 2018

@author: baman
"""
from stack_program import Stack
def decimal_2(dec_number):
    """
        it will convert given number to the decimal number.
    """
    rem_stack = Stack()
    while(dec_number>0):
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2
    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())
    return bin_string

        