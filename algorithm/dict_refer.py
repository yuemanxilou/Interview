#! /usr/bin/python
# coding:utf-8
__author__ = 'weiyufeng'

#创建字段方法
items = [('name', 'earth'), ('port', 80)]
dict2 = dict(items)
print dict2

dict1 = dict((['name', 'earth'], ['port', 80]))
print dict1

dict1 = {}.fromkeys(('x', 'y'), -1)
print dict1

dict2 = {}.fromkeys(('x', 'y'))
print dict2

dict3 = {}.fromkeys(('x', 'y'), 0)
print 'dict3: %s' % dict3


items = [('name','earth'), ('port',80)]
dict4 =dict(items)
print 'dict4: %s' % dict4
print dict((['name', 'earth'],['port', 80]))