#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print('The target list is: ', a)

b = [x for x in a if x%2==1]
print('The new list that has only the even elements of previous list is: ')
print(b)

c = filter(lambda x:x%2!=0, a)
print('The new list that has only the even elements of previous list is: ')
print(list(c))