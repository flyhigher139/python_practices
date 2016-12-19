#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 

(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
    For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

n = input('Please input a number: ')
n = int(n)

# The simplest solution
res = []
for i in range(2, n):
    if n % i == 0:
        res.append(i)

res.append(1)
res.append(n)

res.sort()

print('The following are divisors of your input number: ')
print(res)

# A more efficient solution

from math import sqrt

x = int(sqrt(n))

res2 = []
for i in range(2, x):
    if n % i == 0:
        res2.append(i)
        res2.append(n//i)
        
if n == x * x:
    res.append(x)

res2.append(1)
res2.append(n)

res2.sort()

print('The following are divisors of your input number calculated by another way: ')
print(res2)