#! /bin/env python
# -*- coding: utf-8 -*-

gv = "this is a global var";

def test(v1):
    v2 = "this is a locals var";
    print locals();
    
print globals();

print test("paramater is local var");
