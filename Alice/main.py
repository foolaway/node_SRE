#!/usr/bin/env python3
# -*- conding:utf-8 -*-
from Alice import Alice
#from Bauer import Bauer
from Dad import Dad
from Orange import Orange
from Apple import Apple
from Hotdog import Hotdog



if __name__ == '__main__':
    def inpA():
        try:
            global x,y,z
            x, y, z = input("请输入购买了多少个苹果，多少个橙子，多少火腿，中间用逗号分开：").split(',')
        except:
            print("输入错误，请重新输入")
            inpA()

    inpA()

    #调用苹果类
    APP = Apple(int(x))
    print("购买了%d个苹果"  %APP.apply_num)


    #调用橙子类
    ORA = Orange(int(y))
    print("购买了%d个橙子" %ORA.orange_num)

    #调用热狗类
    HD = Hotdog(int(z))
    print("购买了%d根热狗" %HD.hotdog_num)

    print("购买好后，售货员送了两个篮子，一个篮子装水果，另一个篮子装热狗")




    def inpB():
        try:
            global x1,y1,z1
            x1, y1, z1 = input("\n给了爸爸多少个苹果，多少个橙子，多少火腿，中间用逗号分开：").split(',')
        except:
            print("输入错误")
            inpB()

    inpB()

    x = int(x) - int(x1)
    y = int(y) - int(y1)
    z = int(z) - int(z1)
    APP = Apple(int(x))
    ORA = Orange(int(y))
    HD = Hotdog(int(z))
    print("水果篮里还有苹果%s个，橙子%s个，另一个篮子还有%s根热狗\n" % (x, y, z))

    DA = Dad
    DA.thanl_dad()
    AL = Alice
    AL.thankA()


