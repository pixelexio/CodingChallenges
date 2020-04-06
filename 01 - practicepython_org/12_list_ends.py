#!/usr/bin/env python3.8.x
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 12 - practicepython.org

Write a program that takes a list of numbers and makes a new list of only 
the first and last elements of the given list. For practice, write this code inside a function. 
"""

import random

#a = [5, 10, 15, 20, 25, 145]
a = sorted(random.sample(range(1,30), random.randint(5, 10)))

def firstandlast(list):
    return [list[0], list[len(list)-1]]

print("The random list:", a)
print("First and last :", firstandlast(a))