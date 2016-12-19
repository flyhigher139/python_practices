#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

word = raw_input('Please input a string for check: ')

# Method 1:
reverse_word = word[::-1]

if word == reverse_word:
    print 'The word you input is a palindrome'
else:
    print 'The word you input is not a palindrome'

# Method 2:
is_palindrome = True
length = len(word)
for i in xrange(0, length/2):
    if word[i] != word[length-1-i]:
        is_palindrome = False
        break

if is_palindrome:
    print 'The word you input is a palindrome'
else:
    print 'The word you input is not a palindrome'