#! /usr/bin/env python
# -*- coding: utf-8 -*-

t = (1,2,3,4);
d = dict(name = "zhangjl",age = "19",info = "^_^");
def test(*argv1,**argv2):
    print argv1;
    print argv2;

test(1,2,3,4,name = "zhangjl",age = "19",info = "^_^");

u'''等价于上面的调用'''
test(*t,**d);
