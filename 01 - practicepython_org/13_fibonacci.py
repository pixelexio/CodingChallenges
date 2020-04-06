#!/usr/bin/env python3.8.x
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 13 - practicepython.org

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
"""

def fibonacci(user_input):
    sequence = [1, 1]
    for i in range(user_input - len(sequence)):
        sequence.append(sequence[-2] + sequence[-1])
    return sequence

while True:
  try:
     print(fibonacci(int(input("How many fibonacci numbers would you like to print?: "))))
     break
  except ValueError:
     print("\nIvalid input. Input should be a integer.")
     continue