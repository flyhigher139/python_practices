#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

- Instead of printing the elements one by one, 
make a new list that has all the elements less than 5 from this list in it and print out this new list.

- Write this in one line of Python.

- Ask the user for a number and return a list that contains only elements from the original list that are smaller than the number given by the user.
'''

numbers = raw_input('Please input a group of numbers seperated by ",": ')
number_list = [int(number.strip()) for number in numbers.split(',')]

print 'Those are numbers in the group smaller than 5: '
for number in number_list:
    if number < 5:
        print number

##########################
# For Extras:
##########################

print 'Filter numbers smaller than 5 to a new list: '
# Method 1:
new_number_list = [number for number in number_list if number<5]
print 'filter list in Method 1: ', new_number_list

# Method 1:
new_number_list2 = filter(lambda x:x<5, number_list)
print 'filter list in Method 2: ', new_number_list2

ceiling = raw_input('Please input a custom filter number: ')
ceiling = int(ceiling)

new_number_list3 = filter(lambda x:x<ceiling, number_list)
print 'The following are numbers that are smaller than {0}: '.format(ceiling), new_number_list3