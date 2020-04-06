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

a = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]

# the easy way using sets that does not allow duplicates
def remove_duplicates1(list_name):
    return list(set(list_name))

# using loop to check for duplicates
def remove_duplicates2(list_name):
  new_list = []
  for i in list_name:
    if i not in new_list:
      new_list.append(i)
  return new_list

print(a)
print(remove_duplicates1(a))
print(remove_duplicates2(a))