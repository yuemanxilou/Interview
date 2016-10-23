#! /usr/bin/python
# coding:utf-8
__author__ = 'Michael'

def partition(alist, start, end):
    pivot = alist[start]
    first = start + 1
    last = end
    done  = True

    while not done:
        while alist[first] <= pivot and alist[first] <= pivot:
            first = first + 1
        while alist[last] >= pivot and alist[last] >= pivot:
            last = last -  1
        if first > last:
            done = True
        else:
            tmp = alist[first]
            alist[first] = alist[last]
            alist[last] = tmp

    tmp = alist[start]
    alist[start] = alist[last]
    alist[last] = tmp
    return last

def quick_sort(alist, start, end):
    if start < end:
        mid = partition(alist, start, end)
        quick_sort(alist, start, mid-1)
        quick_sort(alist, mid+1, end)


if __name__ == '__main__':
    L = [5,6,78,9,0,-1,2,3,-65,12]
    quick_sort(L, 0, len(L)-1)
    print L