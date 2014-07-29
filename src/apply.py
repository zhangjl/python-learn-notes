#! /usr/bin/env python
# -*- coding: utf-8 -*-

def add(x,y):
    return x + y;

def sub(x,y):
    return x - y;

def apply(func,x,y):
    return func(x,y);

print apply(add,3,1);
print apply(sub,3,1);
