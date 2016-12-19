#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)


Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''


rule = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}

results = {
    0: 'Same input',
    1: 'playerA wins!',
    2: 'playerB wins!'
}

def validate_input(val):
    if val in rule.keys():
        return True
    return False

def valid_input_factory(player):
    val = input('Input for {0}: '.format(player)).lower()
    while not validate_input(val):
        print('Invalid input, input again...')
        val = input('Input for {0}: '.format(player)).lower()

    return val


def compare(input_a, input_b):
    if input_a == input_b:
        result = 0
    elif rule[input_b] == input_a:
        result = 1
    else:
        result = 2
    return result

def game():
    play_flag = 'yes'
    while not play_flag=='quit':
        print('Choices for input: rock, paper, scissors')
        input_a = valid_input_factory('playerA')
        input_b = valid_input_factory('playerB')

        print('player_A: {0}'.format(input_a), 'player_B: {0}'.format(input_b))

        res = compare(input_a, input_b)
        print(results[res])

        play_flag = input('Press <quit> to quit the game. \nPress any thing else to continue...')


if __name__ == '__main__':
    game()

