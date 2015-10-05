#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

n = raw_input('Please input a number: ')

n = int(n)

if n % 2 == 0:
    print 'The number you input is even'

else:
    print 'The number you input is odd'

if n % 4 == 0:
    print 'and the number is a multiple of 4'

print 'Check if a number could be divided evenly by another one: '

num = raw_input('Please input a number to check: ')
divider = raw_input('Please input a divider number: ')

num = int(num)
divider = int(divider)

remainder = num % divider

if remainder == 0:
    print '{0} could be divided by {1} evenly'.format(num, divider)
else:
    print '{0} could not be divided by {1} evenly, the remainder is {2}'.format(num, divider, remainder)