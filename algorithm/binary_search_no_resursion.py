#! /usr/bin/python
# coding:utf-8
__author__ = 'Michael'

def binary_search(alist, start, end, value):
    while start <= end:
        mid = (start + end)/2
        if alist[mid] < value:
            start = mid +1
        elif alist[mid] > value:
            end  =mid-1
        else:
            return mid
    return -1

if __name__ == '__main__':
    L = [-65, -1, 0, 2, 3, 5, 6, 9, 12, 78]
    pos = binary_search(L, 0, len(L)-1, 6)
    print pos