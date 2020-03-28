#!/usr/bin/env python3.8.x
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 06 - practicepython.org

Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

user_input = str(input("\nPlease enter a word to check: "))
input_reverse = user_input[::-1]
print(f"Input   '{user_input}'")
print(f"Reverse '{input_reverse}'")
if user_input == input_reverse:
    print(f"\nYes, '{user_input}' is a palindrome")
else:
    print(f"\nNo, '{user_input}' is a palindrome")