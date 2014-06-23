# /usr/bin/env python
# -*- coding: utf-8 -*-

# 1. Module documentation
'''this is a test module'''

# 2. Module imports
import sys;
import os;

# 3. Variable declarations
debug = True;

# 4. Class declarations
class FooClass (object) : 
    '''Foo Class'''
    pass;

# 5. Function declarations
def test() : 
    '''test function'''
    if debug:
        print "run test()";

# 6. "main" body
if "__main__" == __name__:
    test();
