#! /bin/env python
# -*- coding: utf-8 -*-

def read(filename):
    f = file(filename,"r");
    for line in f:
        if isinstance(line,unicode):
            print "unicode";
            print line.encode("utf-8");
        else:
            print "not unicode";
            print line.decode("gbk").encode("utf-8");
    f.close();

read("txt_gbk.txt");
