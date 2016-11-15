#! /usr/bin/python
# coding:utf-8
__author__ = 'Michael'

def bubblesort(alist):
    if len(alist) == 0:
        return -1
    for i in xrange(len(alist)-1, 0, -1):
        for j in xrange(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


if __name__ == '__main__':
    L = [5,6,78,9,0,-1,2,3,-65,12]
    bubblesort(L)
    print L