#! /usr/bin/python
# coding:utf-8
__author__ = 'weiyufeng'

tu = (1,2,3,4)
print '{0} {2} {3} {1}'.format(*tu)


lst  =range(5)
it = iter(lst)
print it
print it.next()
print it.next()


L = [1,2,3]
for i in enumerate(L):
    print i, type(i)

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw


func(1, 2)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)

args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)

print func.__name__



