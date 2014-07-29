# -*- coding: utf-8 -*-

''' 浅拷贝 '''
l = [['a','b'],['c','d']];
l1 = list(l);
l1[0][0] = "A";
print l1;   # [['A','b'],['c','d']]
print l;    # [['A','b'],['c','d']]
