#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 07 - practicepython.org
Let’s say I give you a list saved in a variable: 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""

# given list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# make new list with with even numbers
list_even = [x for x in a if x % 2 == 0]

# make new list with with odd numbers
list_odd = [ x for x in a if x % 2 != 0]

# print the lists
print(f"\nGiven list: {a}")
print(f"Even: {list_even}")
print(f"Odd : {list_odd}")