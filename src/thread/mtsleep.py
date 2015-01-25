#! /usr/bin/env python
#! -*- encoding: utf-8 -*-

import threading
import time

loops = [4, 2]

def loop(nloop, nsec):
    print 'start loop ', nloop, ' at: ', time.ctime()
    time.sleep(nsec)
    print 'loop ', nloop, ' done at: ', time.ctime()

def main():
    print 'starting at: ', time.ctime()
    threads = []

    nloops = range(len(loops))

    for i in nloops:
        threads.append(threading.Thread(target = loop, args = (i, loops[i])))

    for i in nloops:
        threads[i].start()

    '''
    for i in nloops:
        threads[i].join()
    '''

    print 'all DONE at: ', time.ctime()


if '__main__' == __name__:
    main()
