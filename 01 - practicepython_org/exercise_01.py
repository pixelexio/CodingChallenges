#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 01 - practicepython.org
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras: 
Add on to the previous program by asking the user for another number 
and printing out that many copies of the previous message.
"""

import datetime

while True:
    userName = input("What is your first name?: ")
    if userName.isalpha():
        break
    print("\nIvalid input. Your age should be a number.")
    
while True:
    userAge = input("What is your age?: ")
    if userAge.isdigit():
        break
    print("\nIvalid input. Your age should be a number.")

year = datetime.date.today().year
years = 100 - int(userAge)

print("\nHello {}, you are {} years old.".format(userName, userAge))
print("You will turn 100 in {} years.\n".format(years))

# Extras
while True:
    anumber = input("Enter a number from 1 to 10: ")
    if anumber.isnumeric() and int(anumber) in range(1, 11):
        break
    print("\nIvalid input.")

print("\nThank you! I will now print the last answer {} times :)".format(anumber))
for x in range(0, int(anumber)):
    print("You will turn 100 in {} years.".format(years))