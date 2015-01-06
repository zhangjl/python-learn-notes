#! /usr/bin/env python
#! -*- encoding: utf-8 -*-

class P(object):
    def __del__(self):
        pass

class C(P):
    def __init__(self):
        print "init"

    def __del__(self):
        P.__del__(self)
        print "delete"

if '__main__' == __name__:
    c1 = C()
    c2 = c1
    c3 = c1

    del c1 # 没有输出
    del c2 # 没有输出
    del c3 # 输出delete

