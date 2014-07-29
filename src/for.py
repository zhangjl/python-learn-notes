#! /usr/bin/env python
# -*- coding: utf-8 -*-

count = 0;
while count < 9:
    print count;
    count += 1;

print "#" * 20;

for i in 1,2,3,4:
    print i;

print "#" * 20;

for i in [x + 1 for x in range(0,10)]:
    print i;

print "#" * 20;
