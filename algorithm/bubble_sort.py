#! /usr/bin/python
# coding:utf-8
__author__ = 'Michael'


def bubbleSort(alist):
    for i in xrange(len(alist)-1,0, -1):
        for j in xrange(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

if __name__  == '__main__':
    L = [5,6,78,9,0,-1,2,3,-65,12]
    bubbleSort(L)
    print L