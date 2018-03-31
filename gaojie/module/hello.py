#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__='Dalao'

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello,World')
    elif len(args)==2:
        # s表示一个str类型的参数,argv第一个值是文件名,[1]表示第二个值
        print("Hello,%s!"%args[1])
    else:
        print("Too many arguments!")

if __name__=='__main__':
    test()
