#! /bin/env python
# -*- coding: utf-8 -*-

gv = "this is a global var";

def test(v1):
    v2 = "this is a locals var";
    def inner():
        print v2;
    print locals();
    
print globals();

print test("paramater is local var");

def test1():
    gv = "this is a local var";
    print gv; # this is a local var

print gv; # this is a global var
