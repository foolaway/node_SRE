#!/usr/bin/env python3
# -*- conding:utf-8 -*-
from Person import Person
from Apple import Apple

class Dad(Person,Apple):
    def __init__(self, name:str,apple_num:int):
        super().__init__(apple_num)
        super(Person,self).__init__(name)

    def thanl_dad():
        print("thank,my daughter，i like you")


if __name__ == '__main__':
    a = Dad(2,1)
    pass
