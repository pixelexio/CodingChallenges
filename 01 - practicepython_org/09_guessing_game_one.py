#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 09 - practicepython.org

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Extras: 
1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, print this out. 
"""

import random

random_number = random.randint(1,9)
guess = 0
guess_count = 0

while guess != random_number and guess != "exit":
    guess = input("Enter a guess between 1 to 9: ")

    if guess == "exit":
        break

    guess = int(guess)
    guess_count += 1

    if guess < random_number:
        print("Your guess is too low")
    elif guess > random_number:
        print("Your guess is too high")
    else:
        if guess_count == 1:
            print("\nYes, you got it right on first guess!")
        else:
            print("\nYes, you got it right with", guess_count, "guesses!")
input()

