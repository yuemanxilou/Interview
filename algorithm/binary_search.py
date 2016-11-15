#! /usr/bin/python
# coding:utf-8
__author__ = 'Michael'

def binary_search(alist, start, end, value):
    if start > end:
        return -1
    else:
        mid = (start + end)/2
        if alist[mid] > value:
            return binary_search(alist, start, mid -1, value)
        elif alist[mid] < value:
            return binary_search(alist, mid + 1, end, value)
        else:
            return mid

if __name__ == "__main__":
    L = [-65, -1, 0, 2, 3, 5, 6, 9, 12, 78]
    pos = binary_search(L, 0, len(L)-1, 78)
    print pos