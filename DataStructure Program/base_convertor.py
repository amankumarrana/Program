# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:41:01 2018

@author: baman
"""

from stack_program import Stack

def base_convertor(dec_number, base):
    """
        Program will convert the binary no based on the base.
    """
    digits = "0123456789ABCDEF"
    st = Stack()
    while(dec_number>0):
        rem = dec_number % base
        st.push(rem)
        dec_number = dec_number // base
    new_str = ''
    while not st.is_empty():
        new_str = new_str + digits[st.pop()]
    return new_str