#! /usr/bin/python
# coding:utf-8
__author__ = 'Michael'

def select_sort(alist):
    for i in xrange(len(alist)-1, 0, -1):
        pos = 0
        for j in xrange(1,i+1):
            if alist[j] > alist[pos]:
                pos = j
        alist[i], alist[pos] = alist[pos], alist[i]


if __name__ == '__main__':
    L = [5,6,78,9,0,-1,2,3,-65,12]
    select_sort(L)
    print L