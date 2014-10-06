#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cjson
currentDir = os.path.dirname(os.path.abspath(__file__))
readFile = currentDir + "/test.txt"
writeFile = currentDir + "/test_w.txt"
readFileJson = currentDir + "/test.json"

f = open(readFile,'r')
print f.read()
f.close()

f = open(readFile,'r')
print f.readlines()
f.close()

f = open(writeFile,'w')
f.writelines('''this is a test
hello China
^_^
''')
f.close()

f = open(writeFile,'a+')
f.truncate()
f.close()

######################################
fJson = open(readFileJson,'r')
print cjson.decode(fJson.read())
fJson.close()
