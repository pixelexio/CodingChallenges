#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 03 - practicepython.org

Write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

Extras: 
1. stead of printing the elements one by one, make a new list that has all 
   the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python. 
3. Ask the user for a number and return a list that contains only elements 
   from the original list a that are smaller than that number given by the user
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(f"\nOriginal list: \n{a}")

print("\nPrint elements lower than 5:")
for x in a: 
    if x < 5:
        print(x)

# Extras 1: make new lists with the elements
print("\nExtras 1: Make a new list of the elements and print:")
b = []
for x in a: 
    if x < 5:
        b.append(x)
print(b)

print("\nPrint elements of the list without brackets:")
print(*b, sep=", ")

# Extras 2: One line code (two examples)
print("\nExtras 2: Same code in one line (with and without brackets):")
print([x for x in a if x < 5])
print(*[x for x in a if x < 5], sep=", ")

# Extras 3: User input
print("\nWhat is the highest number you want to print?")

while True:
    num = input("Enter a number from 0 to 89: ")
    if num.isnumeric() and int(num) in range(0, 90):
        num = int(num)
        break
    print("\nIvalid input.")

c = []
for y in a: 
    if y <= num:
        c.append(y)
if len(c) == 0:
    print(f"\nThere is no element in the list equal or lower than {num}:")
elif len(a) == len(c):
    print(f"\nAll elements in the list equal or lower than {num}:")
    print(c)
if len(c) == 1: # in case the list is changes (lowest number of elements is 2 with current list).
    print(f"\nThere is 1 element in the list equal or lower than {num}:")
else:
    print(f"\nThere is {len(c)} elements in the list equal or lower than {num}:")
    print(c)