# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:43:55 2021

@author: CQ-PRO
"""
'''
import threading
import _thread
import time
def print_time( threadName , delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count +=1
        print("%s : %s" %(threadName, time.ctime(time.time() )))
try:
    _thread.start_new_thread( print_time,("Thread_1",2, ))
    # 调用 _thread 中的 start_new_thread() 开始新的线程
    threading.start_new_thread( print_time,("Thread_1",4, ))
except:
    print("Error:无法启动线程")
while 1:
    pass
'''


import _thread
import time
def print_time( threadName , delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count +=1
        print("%s : %s" %(threadName, time.ctime(time.time() )))
try:
    _thread.start_new_thread( print_time,("Thread_1",2, ))
    # 调用 _thread 中的 start_new_thread() 开始新的线程
    _thread.start_new_thread( print_time,("Thread_1",4, ))
except:
    print("Error:无法启动线程")
while 1:
    pass
'''
# 普通方式进行
'''
from random import randint
from time import time,sleep
import os
def download_task(filename):
    print('开始下载%s...' %filename)
    time_to_download = randint(5,10)
    k = time_to_download
    print('>',end=' ')
    while k >= 0:
        os.system("clear")
        print('=',end=" ")
        k-=1
    sleep(time_to_download)
    print('>完成')
    print()
    print('%s下载成功！耗时%d秒'%(filename,time_to_download))

def  main():
    start = time()
    download_task('Python从入门到入坟')
    download_task('Peking Hot.avi')
    end=time() 
    print('总耗时了%.2f秒.'%(end-start))
    
if __name__ == '__main__':
    main()
  '''  
    
# 运行进程
'''
from multiprocessing import Process 
import os
def Number(self):
        os.system(2)
        i=1
        if i < 53:
            print(i,end='')
            i+=1
        
        
def Letter(self):
    letter = ['A','B','C','D','E','F','G','H','I','J',
              'K','L','M','N','O','P','Q','R','S','T',
              'U','V','W','X','Y','Z'] 
    i=0
    print(letter[i])
    i+=1
    
def main():   
    p1 = Process(target=Number, args=(None, ))
    p1.start()
    p2 = Process(target=Letter, args=(None, ))
    p2.start()
    p1.join()
    p2.join()
if __name__ == '__main__':
    main()
'''

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
 '''  

的喇叭


# HomeWork 
# 7.3



# 正则表达式








































































































































































































