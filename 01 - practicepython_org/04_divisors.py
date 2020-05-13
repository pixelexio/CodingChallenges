#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 04 - practicepython.org

Create a program that asks the user for a number 
and then prints out a list of all the divisors of that number.
"""

# get input with int validation
print("")
while True:
  try:
     num = int(input("Please enter a number to to list the divisors: "))
     break
  except ValueError:
     print("\nIvalid input. Input should be a integer.")
     continue

# loop range of numbers and make a list of divisors
divisors = []
for x in range(1,num+1):
    if(num%x==0):
        divisors.append(x)

# print the result
print(f"\nThe divisors of {num} is:")
print(*divisors, sep=", ")