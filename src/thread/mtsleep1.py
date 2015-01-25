#! /usr/bin/env python
#! -*- encoding: utf-8 -*-

import threading
import time

loops = [4.0, 2.0]

class ThreadFunc(object):

    def __init__(self, func, args, name = ''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print 'start loop ', nloop, ' at: ', time.ctime()
    time.sleep(nsec)
    print 'loop ', nloop, ' done at: ', time.ctime()

def main():
    print 'starting at: ', time.ctime()
    threads = []

    nloops = range(len(loops))

    for i in nloops:
        threads.append(threading.Thread(target = ThreadFunc(loop, (i, loops[i]), loop.__name__)))

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all DONE at: ', time.ctime()


if '__main__' == __name__:
    main()
