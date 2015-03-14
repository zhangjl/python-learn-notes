#! /usr/bin/en python
# -*- coding: utf-8 -*-

n2 = 2
n3 = 3
n4 = 4

'''
version 1
'''
def wrapper(fn):
    def inner(*args):
        return fn(args[0],args[1]) + 1;

    return inner;

@wrapper
def add(x,y):
    return x + y;

print add(1,2); # 4

'''
version 2
'''
def wrapper2(x):
    def inner(fn):
        def inner2(*args):
            return fn(args[0],args[1]) + x;
        return inner2

    return inner;

@wrapper2(n2)
def addx(x,y):
    return x + y;

print addx(1,2) # 5

'''
verision 3
'''
def wrapper3(x):
    print 'wrapper3'
    def inner3(fn):
        print 'inner3'
        def inner5(*args):
            print 'inner5'
            return fn(args[0],args[1]) + x;
        return inner5

    return inner3;

def wrapper4(x):
    print 'wrapper4'
    def inner4(fn):
        print 'inner4'
        def inner6(*args):
            print 'inner6'
            return fn(args[0],args[1]) + x;
        return inner6

    return inner4;

@wrapper3(n3)
@wrapper4(n4)
def addxy(x,y):
    return x + y;

print addxy(1,2) # 10
# wrapper3(n3)(wrapper4(n4)(addxy))(x,y)

