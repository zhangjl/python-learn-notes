#! /usr/bin/env python
#! -*- encoding: utf-8 -*_

import threading

class MyThread(threading.Thread):

    def __init__(self, func, args, name = ''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        self.res = self.func(*self.args)
