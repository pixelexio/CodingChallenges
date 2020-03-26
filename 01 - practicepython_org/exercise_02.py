#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 02 - practicepython.org

Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user.

Extras: 
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
print("")
while True:
  try:
     num = int(input("Please enter a number to check: "))
     break
  except ValueError:
     print("\nIvalid input. Input should be a integer.")
     continue

while True:
  try:
     check = int(input("What number would you like to devide by: "))
     break
  except ValueError:
     print("\nIvalid input. Input should be a integer.")
     continue

if num % 4 == 0:
    oddeven = "\n{} is an even number and a multiple of 4".format(num)
elif num % 2 == 0:
    oddeven = "\n{} is an even number".format(num)
else:
    oddeven = "\n{} is an odd number".format(num)

if (num % check) == 0:
    devides = "and yes, it divides evenly by {}".format(check)
else:
    devides = "and no, it does not divide evenly by {}".format(check)

print(oddeven, devides)
