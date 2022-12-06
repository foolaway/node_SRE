#!/usr/bin/env python3
# -*- conding:utf-8 -*-
from Person import  Person
from Fruit_store import Fruit_store
from Bread_store import Bread_store



class Alice(Person,Fruit_store,Bread_store):
        def __init__(self, name:str):
            super().__init__(name)
           # self.name = name

        def a(self):
            print(self.name)

        def thankA():
            print("I lOVE YOU TOO")




if __name__ == '__main__':
    Ali = Alice(1)
    Ali.a()



    pass
