#! /usr/bin/python
# coding:utf-8
__author__ = 'weiyufeng'

L = [1,2,3,4,5,6,7,8,9]

d ={v: v*10 for v in L}
print d


li = [1,2,3,4,5,6,7,8,9]
print [x**2 for x in li if x >5]