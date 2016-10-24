#! /usr/bin/python
# coding:utf-8
__author__ = 'weiyufeng'

class Node(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

def deep(root):
    if not root:
        return
    print root.data
    deep(root.left)
    deep(root.right)

def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) +1

def isSameTree(p ,q):
    if p == None and q == None:
        return True
    elif p and q:
        return p.data == q.data and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == "__main__":
    # deep(tree)
    l = maxDepth(tree)
    print l