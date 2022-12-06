#!/usr/bin/env python3
# -*- conding:utf-8 -*-
from Store import  Store

class Fruit_store(Store):
    def __init__(self,store_name:str,type:str,apply,orange):
        super().__init__(store_name,type)
        self.__apply = apply
        self.__orangle =orange

    def show_store_name(self):
        print(self.store_name)


if __name__ == '__main__':
    f = Fruit_store('s','b','i','s')

    pass
