#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ask the user for a number and determine whether the number is prime or no
'''

from __future__ import print_function
from math import sqrt
import sys


if sys.version_info < (3, 0):
    # python 2
    input = raw_input
    range = xrange

def check_prime(n):
    x = int(sqrt(n))

    for i in range(2, x+1):
        # print(i)
        if n % i == 0:
            return False

    return True

x = input('Please input a number:')

try:
    x = int(x)
except ValueError:
    print('Input invalid. You need to input a number')

print('Prime check: ', check_prime(x))
