#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 05 - practicepython.org

Take two lists and write a program that returns a list 
that contains only the elements that are common between the lists.
Make sure your program works on two lists of different sizes.

Extras:
1. Randomly generate two lists to test this
2. Write this in one line of Python
"""

import random as r

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(f"\nThe provided lists: \na = {a}\nb = {b}")

# make a new list containing elements in both a and b
print("\nIntersection of list a and b:")
if (set(a) & set(b)): 
    print(list(set(a) & set(b))) 
else: 
    print("No elements in both lists")  

# Extras 1: random generate list lengths and numbers
print("\nIntersection of two lists with random lenght and numbers:")
def rand_lists_isect(out_min, out_max, size_min, size_max):
    list1 = [r.randint(out_min,out_max) for _ in range(r.randint(size_min,size_max))]
    list2 = [r.randint(out_min,out_max) for _ in range(r.randint(size_min,size_max))]
    print(f"List1: {list1} \nList2: {list2}")
    print(f"Intersection: {set(list1).intersection(set(list2))}")
rand_lists_isect(1,30,15,30)

# Extras 2: print intersection of two list in one line of code
print("\nThe intersection of two lists with onle line of code:")
print(set(a).intersection(set(b)))