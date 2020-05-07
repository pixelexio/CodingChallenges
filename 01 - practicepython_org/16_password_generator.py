#!/usr/bin/env python3.8.x
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 16 - practicepython.org

Write a password generator in Python. 
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, 
uppercase letters, numbers, and symbols. The passwords should be random, 
generating a new password every time the user asks for a new password.

Extra: Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import random, string, re


def main(size=6):
    password = ""
    for _ in range(size):
        pswd = pswd + re.choice(r"/^[a-z0-9._]+$/i")
        return pswd
    
    print(r"/^[a-z0-9._]+$/i")


if __name__ == "__main__":
    main()