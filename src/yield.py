#! /usr/bin/env python
#! -*- encoding: utf-8 -*-

def func1(i):
    yield i
    #return i + 1

def counter(start):
    count = start
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1

if '__main__' == __name__:
    #print func1(1).next()

    count = counter(5)
    print count.next()
    print count.next()
    print count.send(9)
    print count.next()
    print count.next()

    count.close()
