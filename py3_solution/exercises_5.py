#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

- Randomly generate two lists to test this
- Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

######################################
# Randomly generate lists a and b
######################################
length1 = random.randint(10,20)
a = [random.randint(1,50) for i in range(length1)]

length2 = random.randint(10,20)
b = [random.randint(1,50) for i in range(length2)]

print('list a: ', a)
print('list b: ', b)

#######################################
# Calculate intersection of a and b
#######################################

# method 1:
res = []
for i in a:
    if i in b:
        res.append(i)

# Remove duplacates
res = list(set(res))

print('Method 1:')
print('The intersection of a&b is: ', res)

# method 2:
res = filter(lambda x:x in b, a)
res = list(set(res))
print('Method 2:')
print('The intersection of a&b is: ', res)

# method 3:
res = list(set(a) & set(b))
print('Method 3:')
print('The intersection of a&b is: ', res)

