#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Example():
    def __init__(self,my_dict = {}):
        self.my_dict = my_dict;

    def change_my_dict(self):
        self.my_dict[5] = "five"

if "__main__" == __name__:
    example = Example()
    example.change_my_dict()
    example2 = Example()

    print example.my_dict, example2.my_dict
    # {5: "five"} {5: "five"}

    example = Example({})
    example.change_my_dict()
    example2 = Example({})

    print example.my_dict, example2.my_dict
    # {5: "five"} {}
