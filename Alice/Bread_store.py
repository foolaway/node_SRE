#!/usr/bin/env python3
# -*- conding:utf-8 -*-
from Store import  Store

class Bread_store(Store):

    def __init__(self,store_name,type,hotdog):
        super().__init__(store_name,type)
        self.hotdog =hotdog


if __name__ == '__main__':
    pass
