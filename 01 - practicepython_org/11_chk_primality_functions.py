#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 11 - practicepython.org

Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
"""

# get input with int validation
print("")
while True:
  try:
     num = int(input("Please enter a number to to check if prime or not: "))
     break
  except ValueError:
     print("\nIvalid input. Input should be a integer.")
     continue

# loop range of numbers and make a list of divisors
divisors = []
for x in range(1,num+1):
    if(num%x==0):
        divisors.append(x)

# print the result, prime has only 2 dividors.
if len(divisors) == 2:
    print(f"\n{num} is a prime.")
else:
    print(f"\n{num} is not a prime.")
print(f"\nThe divisors of {num} is:")
print(*divisors, sep=", ")