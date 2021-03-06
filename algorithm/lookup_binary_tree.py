#! /usr/bin/python
# coding:utf-8

__author__ = 'weiyufeng'

class Node(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))


def lookup1(stack):
    if not stack:
        return
    root =stack.pop(0)
    if root:
        print root.data
        stack.append(root.left)
        stack.append(root.right)
    lookup1(stack)

def lookup2(root):
    stack = [root]
    while stack:
        current = stack.pop(0)
        print current.data
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
if __name__ == '__main__':

    lookup2(tree)
