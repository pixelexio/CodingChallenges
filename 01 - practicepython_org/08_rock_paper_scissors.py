#!/usr/bin/env python3.8.x
# -*- coding: utf-8 -*-

__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

""" 
Exercise 08 - practicepython.org

Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules: Rock beats scissors, Scissors beats paper, Paper beats rock
"""
# This is version one with one round of game. I will add scoreboard and multiple rounds in later version.

import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

choices = {
  1: "Rock",
  2: "Paper",
  3: "Scissors"
}

welcome = """
   _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._
 ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.
( (                                                         ) )
 ) )               Rock - Paper - Scissors                 ( (
( (             Rock < Paper < Scissors < Rock              ) )
 ) )                   Two player game                      ( (
( (                                                         ) )
 ) )                      pixelexio                        ( (
( (_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._) )
 `._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._,'
"""

cls()
print(welcome)
player1 = input("Enter player 1 name: ")

cls()
print(welcome)
player2 = input("Enter player 2 name: ")

if player1 == "":
    player1 = "Player 1"
if player2 == "":
    player2 = "Player 2"

cls()
print(welcome)
print(f"God luck {player1} and {player2}!")
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock\n")

def player_coice():
    while True:
        choice = input("Enter a number from 1 to 3: ")
        if choice.isnumeric() and int(choice) in range(1, 4):
            return choice
            break
        print("\nIvalid input.")

cls()
print(f"It's your turn, {player1}! Best of luck!\n")

print("1. Rock")
print("2. Paper")
print("3. Scissors\n")
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock\n")
p1_choice = int(player_coice())

cls()
print(f"It's your turn, {player2}! Best of luck!\n")

print("1. Rock")
print("2. Paper")
print("3. Scissors\n")
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock\n")
p2_choice = int(player_coice())

cls()
print(f"\n{player1} played: {choices[p1_choice]} \n{player2} played: {choices[p2_choice]}")

choice_diff = p1_choice - p2_choice 
if p1_choice == p2_choice:
    print(f"\nIts a tie! {player1}, {player2}")
    # p0_wins += 1
elif (choice_diff % 3) == 1:
    print(f"\nPlayer 1 wins! {player1}")
    # p1_wins += 1
elif(choice_diff % 3) == 2:
    print(f"\nPlayer 2 wins! {player2}")
    # p2_wins += 1

"""
Playable for one round, will update with scoreboard and option for best of x rounds
"""