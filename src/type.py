#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Foo: pass
class Bar(object): pass

foo = Foo();
bar = Bar();

print type(Foo);    # <type 'classobj'>
print type(foo);    # <type 'instance'>

print type(Bar);    # <type 'type'>
print type(bar);    # <class '__main__.Bar'>

print type(bar).__name__
print type(Bar).__name__
