# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:08:53 2021

@author: CQ-PRO
"""
# 列表
'''
lizi = ['1','2','aok','1','5','6']
lizi2 = ['1','2']
lizi.pop(0)
#列表.pop() 将列表中的元素弹出 
print(lizi)
lizi.append('2')
#列表.append('数字') 一次只能添加一个元素
print(lizi[1].title())
#列表[].tiele() 转换为标准输出 将首字母大写
lizi.remove('1')
#列表.remove('目标值') 根据值删除元素,只删除第一个指定值元素
print(lizi)
lizi.insert(0,'000')
#列表.insert( , ) 指定位置和元素在任何地方都可以添加
print(lizi)
lizi.sort()
#lizi.sort(reverse=False)升序排列
print(lizi)
lizi.sort(reverse=True)
#lizi.sort(reverse=True) 降序排列
print(lizi)
# lizi2.reverse()
print(lizi2.reverse())
# numbers = list(range(1,151))
#  可以生成数字列表
'''

# 习题四 2
'''
answer = []
for i in range(3,151,3):
    answer.append(i)
print(answer)
'''
'''
# 习题四 3

source=[]
for i in range(0,7):
    source.append(int(input("输入成绩:")))
source.sort()
source.pop(0)
source.pop(-1)
sum=0
for j in  range(0,5):
    sum+=source[j]
print(sum)
'''

# 习题四 4
'''
source=[]
负数,正数,零 = 0,0,0
for i in range(0,7):
    source.append(int(input("输入数字:")))
    if source[i] < 0 :
        负数+=source[i]
    if source[i] > 0 :
        正数+=source[i]
    if source[i]== 0 :
        零+=1
print('正数:%d负数:%d零:%d'%(正数,负数,零))
'''



# 字典 

'''
alien_0={'color':'green','points':'5'}
# print(alien_0['color'])
#创造 '键':'信息','键':'信息' 为关键信息
print(alien_0)
alien_0['x_position']=0
# 添加 键-值对
alien_0['y_position']=25
# 添加 键-值对
print(alien_0)
alien_0['y_position']=20
# 修改键-值对
print(alien_0)
del alien_0['y_position']
# 删除快捷键 必须指定字典名和删除的键
print(alien_0)
'''

'''
Who={'name':'cuiqiang',
     'xing':'cui',
     'age':'22',
     'city of live':'sz'}
print(Who)
print(Who['name'].title())
for k,v in Who.items():
    print(k,':',v) 
# 字典的遍历 特定的格式  字典.items()
'''
# 字典里面嵌套列表
'''
pizza={
       'crust':'thick',
       'toppings':['mushrooms','extra cheese'],
       }
print('6:'+pizza['crust'])
for topping in pizza['toppings']:
    print(topping)
'''

# P96 1
'''
str_1 = "Thank You"
for i in str_1:
    if ord(i) >= 65 and ord(i) <= 90 :
        print(chr(ord(i)+32),end='')   
    elif ord(i) >= 97 and ord(i) <= 122 :
        print(chr(ord(i)-32),end='')
    else:
        print(i,end='')
'''























































































































































































































