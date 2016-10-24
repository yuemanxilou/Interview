#! /usr/bin/python
# coding:utf-8
__author__ = 'weiyufeng'

#使用__new__方法
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1



#共享属性
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        ob =super(Borg, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):
    a = 1

#装饰器
def singleton(cls, *args, **kwargs):
    instances = {}
    def getinstances():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

@singleton
class MyClass:
    pass

#import方法

