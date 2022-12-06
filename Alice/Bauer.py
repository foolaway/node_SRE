#!/usr/bin/env python3
# -*- conding:utf-8 -*-
from Person import  Person
from Fruits_basket import Fruit_basket
from Bread_basket import Bread_basket
from Car import Car


class Bauer(Person,Car,Fruits_basket,Bread_basket):
#    def __init__(self,name:str,car_name:str):
#        super(Person,self).__init__(name)
#        super(Car, self).__init__(car_name)
    pass




if __name__ == '__main__':
    q = Bauer('s','b')
    pass
