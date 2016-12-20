#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Exercise

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''


from __future__ import print_function
import random

try: 
    input = raw_input
except NameError: 
    pass


'''
I uses a compatible way to write the code this time
The following code can run both in python 2 and python 3
'''

num = random.randint(1, 9)

count = 0

def guess_count_message(count):
    if count==1:
        return 'You guessed 1 time'
    else:
        return 'You guessed {0} times'.format(count)

def get_input_number():
    val = input('Input a number between 1 and 9 to guess, or input <exit> to quit: ')
    if val.lower()=='exit':
        val = 0
    else:
        try:
            val = int(val)
        except ValueError:
            val = -1

    return val

while True:
    val = get_input_number()
    # print(val)
    exit_signal = False
    
    while val<=0:
        if val==0:
            exit_signal = True
            break
        else:
            val = get_input_number()

    if exit_signal:
        break


    count+=1

    if val == num:
        print('You guessed exactly right')
        print(guess_count_message(count))
        break

    elif val>num:
        print('You guessed higher')
    else:
        print('You guessed lower')