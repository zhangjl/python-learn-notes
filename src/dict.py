#! /usr/bin/env python
#! -*- encoding: utf-8 -*-

class Foo(object):
    '''test Foo'''

    __slots__ = ['name','age']

    def __init__(self,name,age):
        self.name = name
        self.age = age
        # print self.__dict__ # {'age': '11', 'name': 'zhangjl'}

def test():
    foo = Foo('zhangjl','11')

    print "#" * 100

    print Foo.__dict__

if '__main__' == __name__:
    test()
