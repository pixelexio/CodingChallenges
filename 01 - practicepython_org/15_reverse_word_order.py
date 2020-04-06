#!/usr/bin/env python3.8.x
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 13 - practicepython.org

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extra: Write two different functions to do this - one using a loop and constructing a list, and another using sets.
"""

# version 1 using loop
def reverse_string1(user_string):
    user_list = user_string.split()
    list_items = len(user_list)
    reverse_list = []
    counter = 1
    for item in user_list:
        reverse_list.append(user_list[list_items-counter])
        counter += 1
    print(*reverse_list, sep=" ")

# version 2 using slicing operator
def reverse_string2(user_string):
    user_list = user_string.split()
    reverse_list = user_list[::-1]
    print(*reverse_list, sep=" ")

# version 3 using reversed() function
def reverse_string3(user_string):
    user_list = user_string.split()
    for item in reversed(user_list):
        print(item, end=" ")

# version 4 using one line in a function
def reverse_string4(user_string):
  print(" ".join(user_string.split()[::-1]))

user_input =input("Please input a sentence with multiple words: ")
print("\nUser input:\n" + user_input)

print("\nUsing a loop:")
reverse_string1(user_input)
print("\nUsing a slicing operator:")
reverse_string2(user_input)
print("\nUsing the reversed function:")
reverse_string3(user_input)
print("")
print("\nUsing the one line in function:")
reverse_string4(user_input)
print("")

