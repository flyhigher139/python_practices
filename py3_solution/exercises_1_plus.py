#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Exercise

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)

Print out that many copies of the previous message on separate lines. 
(Hint: the string '\n' is the same as pressing the ENTER button)
'''

import datetime

def get_int_number(key, value):
    try:
        value = int(value)
        return value
    except ValueError:
        print('{key} must be an integer'.format(key=key))
        return None

def main():
    name = input('Please input your name: ')
    age_raw = input('Please input your age: ')

    now = datetime.datetime.now()
    year = now.year

    age = get_int_number(key='age', value=age_raw)
    while not age:
        age_raw = input('Please input your age: ')
        age = get_int_number(key='age', value=age_raw)

    year = year + 100 - age

    msg = 'Hi, {name}, by the year {year} you will be 100 years old'.format(name=name, year=year)
    print(msg)

    copies_raw = input('Please input the number of copies you want the message to duplicate: ')
    copies = get_int_number(key='copies', value=copies_raw)
    while not copies:
        copies_raw = input('Please input your age: ')
        copies = get_int_number(key='copies', value=copies_raw)

    msg = (msg+'\n') * copies

    print(msg)

if __name__ == '__main__':
    main()
