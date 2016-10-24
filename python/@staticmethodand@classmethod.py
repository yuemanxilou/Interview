#! /usr/bin/python
# coding:utf-8
__author__ = 'weiyufeng'

def foo(x):
    print 'exectiong foo(%s)' % (x)


class A(object):
    def foo(self, x):
        print 'executing foo(%s, %s)' % (self, x)

    @classmethod
    def class_foo(cls,x):
        print 'executing class_foo(%s, %s)' % (cls, x)

    @staticmethod
    def static_foo(x):
        print 'execuing static_foo(%s)' % x

a = A()
A.class_foo(1)
a.foo(2)
A.static_foo(3)