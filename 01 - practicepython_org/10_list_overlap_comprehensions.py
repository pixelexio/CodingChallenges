#!/usr/bin/env python3.8.x
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 10 - practicepython.org

Take two lists and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras: 
1. Randomly generate two lists to test this
"""

import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
overlaps = [i for i in set(a) if i in set(b)] # makes list of overlaps with no duplicates

print("List a  :", sorted(a))
print("List b  :", sorted(b))
print("Result  :", overlaps)