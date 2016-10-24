#! /usr/bin/python
# coding:utf-8
__author__ = 'weiyufeng'


def f(x):
    return x*x
print map(f, [1,2,3,4,5])


print map(str, [1,2,3,4,5])


def add(x, y):
    return x + y
print reduce(add, [1,3,5,7])


def fn(x,y):
    return x*10+y
print reduce(fn, [1,3,5,7,9])


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print char2num('1')



    