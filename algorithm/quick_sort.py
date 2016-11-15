#! /usr/bin/python
# coding:utf-8
__author__ = 'Michael'

def partition(alsit, first, last):
    if first > last:
        return -1

    privot = alsit[first]
    left = first + 1
    right = last

    done = False

    while not done:
        while left <= right and alsit[left] <= privot:
            left = left + 1
        while left <= right and alsit[right] >= privot:
            right = right - 1
        if left > right:
            done = True
        else:
            alsit[left], alsit[right] = alsit[right], alsit[left]

    alsit[first], alsit[right] = alsit[right], alsit[first]
    return right

def quick_sort(alist, first, last):
    if first < last:
        pos = partition(alist, first, last)
        quick_sort(alist, first, pos-1)
        quick_sort(alist, pos+1, last)

if __name__ == '__main__':
    L = [5,6,78,9,0,-1,2,3,-65,12]
    quick_sort(L, 0, len(L)-1)
    print L