#! /usr/bin/env python
# -*- coding: utf-8 -*-
x,y = 4,3;

smaller = x if x < y else y
print smaller;

smaller = (x < y and [x] or [y])[0];
print smaller;
