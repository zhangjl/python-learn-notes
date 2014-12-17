#! /usr/bin/env python
#! -*- encoding: utf-8 -*-

def func(*argv1,**argv2):
    print argv1 # (1,2,5)
    print argv2 # {}

def func2(x,y,*argv1,**argv2):
    print x # 1
    print y # 2
    print argv1 # ()
    print argv2 # {}

if '__main__' == __name__:
    func(1,2,5)
    func(*(1,2,5))

    func2(1,2)
    func2(1,**{'y': 2})
    func2(**{'x': 1,'y': 2,})
    func2(1,y = 2,*(),**{})
    # func2(**{}) # error
