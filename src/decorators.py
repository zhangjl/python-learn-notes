#! /bin/env python
# -*- coding: utf-8 -*-

def test(fn):
    def hello(name):
        print fn(name);
    return hello;

@test
def xxx(name):
    return "hello %s" %(name,);

xxx("zhangjl");   # zhangjl
