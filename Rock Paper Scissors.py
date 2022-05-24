#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:13:48 2022

@author: ryan
"""

#ROCK PAPER SCISSORS

import random

choices = ['rock', 'paper', 'scissors']

print('Welcome! Ready to play?')

user = input('enter your name: ') 

print('\nHello' ,user,'!')
print('\nChoose rock, paper or scissors. The computers choice will be random.')

while True:
    
    user_choice = input('rock, paper or scissors? ').lower()
    comp_choice = random.choice(choices)

#results in a tie

    if user_choice == comp_choice:
        print(user, ' chose: ',user_choice)
        print('The computer chose: ',comp_choice)
        print('The result is a TIE')
    
#user wins rock, paper, scissors

    if user_choice == 'rock' and comp_choice == 'scissors':
        print(user, 'chose: ',user_choice)
        print('The computer chose: ',comp_choice)
        print(user, 'WON!!!')
    
    if user_choice == 'paper' and comp_choice == 'rock':
        print(user, 'chose: ',user_choice)
        print('The computer chose: ',comp_choice)
        print(user, 'WON!!!')
    
    if user_choice == 'scissors' and comp_choice == 'paper':
        print(user, 'chose: ',user_choice) 
        print('The computer chose: ', comp_choice)
        print(user, 'WON!!!')
    
#computer wins rock, paper, scissors

    if comp_choice == 'rock' and user_choice == 'scissors':
        print(user, 'chose: ',user_choice)
        print('The computer chose: ',comp_choice)
        print(user, 'lost')
    
    if comp_choice == 'paper' and user_choice == 'rock':
        print(user, 'chose: ',user_choice)
        print('The computer chose: ',comp_choice)
        print(user, 'lost')
    
    if comp_choice == 'scissors' and user_choice == 'paper':
        print(user, 'chose: ',user_choice) 
        print('The computer chose: ', comp_choice)
        print(user, 'lost')

    replay = input('Do you wish to play again? (yes/no): ').lower()

    if replay != 'yes':
        break

print('Thanks for playing!!!')
    