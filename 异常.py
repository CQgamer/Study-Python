# -*- coding: utf-8 -*-
"""
Created on Mon May 24 14:52:10 2021

@author: CQ-PRO
"""

try:
    a,b=int(input("::")),int(input("::"))
    c=a/b
    print(a/b)
except (ZeroDivisionError,ValueError,TypeError) as e:
    # 该语句用于检测，是否是这个异常
    print(e)




import os,time
lizi = "方村牛逼.........."
while True:
    os.system('clear')
    print(lizi)
    time.sleep(0)
    lizi = lizi[1::]+lizi[0]

































































































































































































