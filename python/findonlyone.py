#! /usr/bin/python
# coding:utf-8
__author__ = 'Michael'

def findonlyone(alist):
    length = len(alist)
    if length == 0:
        return -1
    else:
        tmp = alist[0]
        for i in xrange(1, len(alist)):
            tmp = tmp ^ alist[i]

        return tmp
if __name__ == '__main__':
    alist = [2,4,7,6,2,4,6]
    a= findonlyone(alist)
    print a