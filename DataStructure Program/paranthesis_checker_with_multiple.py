# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 13:11:15 2018

@author: baman
"""

from stack_program import Stack

def paranthesis_with_multiple(symbol_string):
    """
        Check parathsesis open and close for multiple type
    """
    st = Stack()
    balanced = True
    index = 0
    while(index < len(symbol_string) and balanced):
        symbol  = symbol_string[index]
        if symbol in '({[':
            st.push(symbol)
        else:
            if st.is_empty():
                balanced = False
            else:
                top = st.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    
    if balanced and st.is_empty():
        print('Brackets matched')
    else:
        print('Brackets Not matched')

def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)