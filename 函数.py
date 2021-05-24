# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 13:35:45 2021

@author: CQ-PRO
"""
'''
def say_hellow():
    print("hellow world")
say_hellow()
'''
'''
def t(a,b=3,c=2):
    sum = a+b+c
    return sum
print(t(1))
'''
'''
def t(a,b=1,c=1):
    sum=a+c+b
    print(sum)
t(1)
'''
'''
print("chiNA".upper())
'''
'''
elems=[(2,8),(4,9),(12,3),(1,"a")]
elems.sorted(key=lambda point:point[0])
print(elems)
# 元素  elem
'''

# def change(a,b):
#     a,b=b,a
#     return a,b
# a,b=175,17
# change(a,b)
# print(a,b)

# def change(list):
#     list[0],list[1]=list[1],list[0]
#     return list
# list_a=[5,17]
# list_a=change(list_a)
# print(list_a)


'''
def elem (n):
    if n==1:
        return 1
    else:
        return n * elem(n-1)
print(elem(10))
/'''

# def add(n):
#     if n ==1:
#         return 1
#     else:
#         n=n+1
#         return add(n-1)
# print(add(5))

'''
def swap(a,b):
    a,b=b,a
    return a,b
a,b=3,5
a,b=swap(a,b)
print(a,b)
'''

# 习题3.2
'''
def mul(i):
    sum = 0
    while sum <= 1000:
        sum+=i*i
        i+=1
    return i-1
print(mul(1))
'''

# 习题3.3
'''
def number(str):
    i=0
    sum=0
    while i < len(str):
        if str[i] == " ":
            sum+=1
        i+=1
    # print(len(str))
    return sum,len(str)
t,k=number(input("请输入句子："))
if k == t:
    print("0")
else:
    print(t+1)
'''

# 习题3.4
'''
def P(str):
    i = 0
    while  i < len(str)/2 :
        if str[i] == str[len(str)-i-1]:
            i+=1
        else:
            return 'No'
    return 'yes'
print(P(input("请输入：")))
''' 

'''
a = 1
if a > 1:
    a+=1
print(a)
'''


#  Github 解释计算

# 1.将M个苹果分成N组每组至少一个苹果有多少种方案
'''
m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1,m+1):
    fm*=num
fn = 1
for num in range(1,n+1):
    fn*=num
fm_n = 1
for num in range (1, m-n + 1):
    fm_n*=num
print(fm//fn//fm_n)
'''
# 求几个部分阶乘 得到分块表达式 000|00|00|0  C3_7  计算


'''
def fac(num):
    sum = 1
    for  i in range(1,num+1):
        sum *= i
    return sum
# 利用函数来代替循环效果


m= int(input('m= '))
n= int(input('n= '))
# print(fac(m) // (fac(n) * fac(m-n)))
print(fac(m) // fac(n) // fac(m - n))
'''


# 使用调用函数，更加简单代码量
'''
import math
m= int(input('m= '))
n= int(input('n= '))
print(math.factorial(m)//math.factorial(n)//math.factorial(m-n))
'''
# 说明： Python的math模块中其实已经有一个名为factorial函数实现了阶乘运算，
# 事实上求阶乘并不用自己定义函数。


# Python 中对函数参数定义不同于其他的 编程语言 
# 函数的参数
'''
def add (a=0,b=0,c=0):
    return a+b+c
print(add(1))
print(add(1,2))
print(add(1,2,3))
'''

'''
from random import randint
def roll_dice(n=2):
    """摇色子"""
    total = 0
    for i in range(n):
        total += randint(1, 6)
    return total

print(roll_dice())
'''

# 跨时空调阅 ！
'''
from  idea 
foo() 
'''
'''
from  idea import *
foo() 
'''
'''
import idea as i
i.foo()
!!! i.add(1,2,3) 
i.ok()
'''

# 练习1：实现计算求最大公约数和最小公倍数的函数。
'''
def min(x,y):
    if x > y:
        return y
    else:
        return x
    
def max(x,y):
    if x > y:
        return x
    else:
        return y
    
def max_gy(x,y):
    for i in range (1,x+1):
        if x%(x+1-i)==0 and y%(x+1-i)==0:
            return x+1-i

def min_gbs(x,y):
    for i in range(y,x*y+1):
        if i%x ==0 and i%y==0:
            return i

x = int(input(""))
y = int(input(""))

max1 = max(x,y)
min1 = min(x,y)

print(min_gbs(min1,max1))
print(max_gy(min1,max1))
'''

# ！！！ 排序反转
'''
for i in range(5,1,-1):
    print(i)
'''

'''
def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
# print(is_palindrome(10201))
'''

# 练习3：实现判断'一个数是不是素'数的函数。
'''
def sushu(num):
    for i in range(2,int(num ** 0.5+1)):
        if num % i == 0:
            return False
    return True
'''
# print(sushu(4))


"""if __name__='__main__':"""
# 了解它的意义   


# if __name__ == '__main__':
#     num = int(input('请输入正整数: '))
#     if is_palindrome(num) and sushu(num):
#         print('%d是回文素数' % num)
#     else:
#         print('NO')

# !!!

# 函数套函数  嵌套  对函数内变量的定义域，只应为与函数里


'''
def foo():
    b = 'hellow'
    
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
if __name__ == '__main__':
    a = 100
    foo()
'''

# 使用全局变量使得  global a 定义a
# 可以a在if下的定义无效
'''
def foo():
    global a 
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 100
'''

'''
def main():
    pass
if __name__ == '__main__':
    main()
'''


def is_num(num):
    temp = num
    list1 = []
    while temp > 0:
        list1.append(temp%10)
        temp = temp // 10
    return list1 == list1[::-1]  
print(is_num(12321))
    











































































































































































































































































