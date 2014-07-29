#! /usr/bin/en python
# -*- coding: utf-8 -*-

def wrapper(fn):
    def inner(*args):
        return fn(args[0],args[1]) + 1;

    return inner;

@wrapper
def add(x,y):
    return x + y;

print add(1,2);
