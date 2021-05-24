# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:50:51 2021

@author: CQ-PRO
"""
# ——XXX——表示系统定义名字
# ——XXX表示类中的私有变量名
'''
class lizi ():
    def a(s):
        print('5')
x =  lizi()
print(x.a())
'''
'''
class People():
    name = 0
    age = 0
    def Me(self,name,age):
        self.name=name
        self.age=age
    def Speak(self):
        print("%d %d" %(self.name,self.age))

x = People(5,5)
x.Speak()
'''
# class people:
#     name = ''
#     age = 0
#     sex = ''
#     def __init__(self,n,a,s):
#         self.name = n
#         self.age = a
#         self.sex = s
#     def speck(self):
#         print(self.name,self.age,self.sex)
# x = people('ok',12,"nan")
# x.speck()


# class Complex:
#     r = 0
#     i = 0 
#     def __init__(self,realpart,imagpart):
#         self.r=realpart
#         self.i=imagpart
#     def speak(self):
#         print(self.r,self.i)
# x=Complex(3.0,-4.5)
# print(x.r,x.i)
# x.speak()


# class Pelple:
#     name=''
#     age = 0
#     sex = ""
#     def __init__(self,n,a,s):
#         self.name = n
#         self.age = a
#         self.sex = s
#     def speck(self):
#         print(self.name,self.age,self.sex)
# x = Pelple('ok',12,"nan")
# x.speck()


#习题五 三.1
'''
class Cirle:
    r = 0
    def __init__(self,radius):
        self.r = radius
        print('圆的面积是：%f'  %(self.r*self.r*3.14))
        print('圆的体积是：%f' %(self.r*self.r*self.r*1/3*3.14))
x = Cirle(4)
print()
y = Cirle(8) 
'''

#习题五 三.2       
'''
import datetime
ny = datetime.datetime.now().year
nm = datetime.datetime.now().month
nd = datetime.datetime.now().day
class student:
    no = 0
    mz = ''
    y = 0
    m = 0
    d = 0
    age = 0
    def __init__(self,no,name,year,moon,day):
        self.no = no
        self.mz = name 
        self.y = year
        self.m = moon
        self.d = day        
    def bir(self,ny,nm,nd):              
        self.age = ny-self.y
        if nm <= self.m:
            pass
        elif nd <= self.d:               
                self.age+=1
        print('姓名:',self.mz,'学号:',self.no,'年龄:',self.age) 
print('现在时间：',ny,':',nm,':',nd)
x = student(8611,'小明',2000,1,1)
x.bir(ny,nm,nd)
'''
'''
class Complex:
    i = 123456
    def __init__(self,one,two):
        self.o = one
        self.t = two
X = Complex(1,2)
print(X.o,X.t)
print(X.i)
'''

#构造方法是固定的名称！！！  __init__()

'''
class people():
    @staticmethod
    def staticmethod():
        print("yanshijingtaide1fangfa1")
people.staticmethod()
c = people()
c.staticmethod()
'''

#静态方法无需传入self参数
#需要添加装饰符@statiemethod








































































































































































































































































