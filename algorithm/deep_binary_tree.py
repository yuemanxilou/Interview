#! /usr/bin/python
# coding:utf-8
__author__ = 'weiyufeng'
class Node(object):
    def __init__(self, value , left = None, right = None):
        self.left = left
        self.right = right
        self.value= value

def deep_binart_tree(root):
    if root is None:
        return -1
    print root.value
    deep_binart_tree(root.left)
    deep_binart_tree(root.right)


def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

if __name__ == "__main__":
    # deep_binart_tree(tree)
    l = maxDepth(tree)
    print l