#!/usr/bin/env python3.8.x
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
print("\nIntersection of two lists with random length and numbers.")
print("Made in a funktion and ran two times to see different results:\n")
def rand_sets_isect(values, size):
    get_rand_set = lambda values, size: {r.randint(*values) for _ in range(r.randint(*size))}
    set1 = get_rand_set(values, size)
    set2 = get_rand_set(values, size)
    print(f"Set 1: {list(set1)}", f"Set 2: {list(set2)}", sep="\n")
    print(f"Intersection: {list(set1.intersection(set2))}\n")
for times in range(2):
    rand_sets_isect( [1,30], [15,30] )




# Extras 2: print intersection of two list in one line of code
print("\nThe intersection of two lists with onle line of code:")
print(set(a).intersection(set(b)))