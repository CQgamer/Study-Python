# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
a = input()
b = input()
c = input()
print(float(a)+float(b)+float(c))
'''


'''
a=9
b,c = 9 , a+2
print(a) #  运算中&做且表示 
print(b)
print(c)
print(a**(c//a+1))
print(a,b,c)
'''


'''
a,b=0,1
print(a and b)
print(b or a)'''

'''
# if循环
a = int(input())
if a < 5:
    print("small\n")
elif a  < 18:
    print("a little")
else :
    print('big')    
'''


'''
def sum(x,y,z) :
    sum = x + y +z
    return sum
x=int(input())
y=int(input())
z=int(input())
print(sum(x,y,z))
'''


'''
price = 50.0 
age = int(input())
if age > 50:
    print("price=%fopopp",price/2)
elif age > 80:
    print("price="+0)
else:
    print("price=",price)
    
    if 1 :
        print("YES!")

'''
# 简单的  猜拳游戏    但是算法繁琐臃肿*****************
# 0:石头  1：剪刀  2：布
'''                               
import random
person = int (input('出手吧！小弟弟:')) 
computer = random.randint(0,2)
print('我出',computer)
if person == 0:
    if computer == 0:
        print('平手')
    elif computer == 1:
        print('you are winner')
        pass
    elif computer == 2:
        print("you are loser")
        pass
    
if person == 1:
    pass
    if computer == 1:
        print('平手')
        pass
    elif computer == 2:
        print('you are winner')
        pass
    elif computer == 0:
        print("you are loser")
    pass

if person == 2:
    pass
    if computer == 2:
        print('平手')
        pass
    elif computer == 0:
        print('you are winner')
        pass
    elif computer == 1:
        print("you are loser")
        pass
    #对   if 和 elif 的应用，区别于其它语言的空格作用
'''


#对  while 的学习
#对  while 的学习
#对  while 的学习
#对  while 的学习
#对  while 的学习
'''
i=1
while i<=100:
    print(i)
    i+=1
'''
# python中没有所谓的{}，区别于他们是进行缩进
#全缩进是  选中+Ctrl  反向缩进是 Shift+Ctrl

#                                 9*9        *************
'''
i = 1
while i <= 9:
    j = 9
    while j >=i:   
        print("%d*%d=%d"%(i,j,i*j),end=' ')
        j-=1
    print()
    i+=1
'''
#print 有换行功能，在其后面增加一个end=" " 
#对print进行了解，其中的数据替换


#                    打印直角三角形  **********************
'''
ge = 1
z = int(input("please enter a number:"))
h=1
while h <= z:
    while ge <= h:
        print("*",end=" ")
        ge+=1
    ge=1
    print()
    h+=1
'''


#                  打印倒着的腰三角形  **********************
'''
ge = 1
z = int(input("please enter a number:"))
h=1
while h <= z:
    while ge <= h:
        print(" ",end=" ")
        ge+=1
    if ge>=h:
            while ge <= h+2*(z-h)+1:
                print("*",end=" ")
                ge+=1
    ge=1
    print()
    h+=1
'''


#对for循环进行学习
#对for循环进行学习
#对for循环进行学习
#对for循环进行学习
#对for循环进行学习


'''
for 临时变量  in  容器 ：
    执行代码
'''


'''
tages='12345678'
for it in tages:
    print(it)
'''

#                                       1-100相加*********
'''
sum = 0
for i in range(1,101):
    sum+=i
print("sum=%d"%sum)
'''

'''
list = ['cn','crz','cq','fc',
        'gjj','gy']
for i in list:
    print(i,end=' ')
'''

#  拳头剪刀布 进阶版本
#  拳头 0
#  剪刀 1
#  布   2

'''
import random
i=0
while i<3:
    me = int(input('请出招：'))
    you = random.randint(0,2)
    if me == you:
        print ("==")
    if me==0 and you ==1:
        print('me')
    elif me==1 and you == 0:
        print('you')
        
    if me == 1 and you == 2:
        print('me')
    elif me ==2 and you ==1:
        print('you')
        
    if me == 2 and you ==0:
        print('you')
    elif me == 0 and you == 2:
        print('me')
    i+=1
'''

# P4 习题二  

#1
'''
knife = float(input("请输入刀具长度："))
if knife <=10 :
    print('可以带上飞机')
elif knife >10:
    print('不好意思，不可以带上飞机')
'''
#2
'''
BMI = 80.5/1.75/1.75
print('小明的体脂BMI%f'%BMI)
if BMI < 18.5:
    print('过轻')
elif BMI >= 18.5 and BMI < 25:
    print('正常')
elif BMI >= 25 and BMI <28:
    print('过重')
elif BMI >=28 and BMI <32:
    print('肥胖')
elif BMI >=32:
    print('严重肥胖')
'''
#3
'''
import random
answer = random.randint(0,100)
print(answer)
i=1
while 1:
    guess = int(input('请输入你的猜测数字'))
    if guess > answer:
        print("大了哦")
    elif guess == answer:
        print('对了')
        break
    else :
        print('小了')
    i+=1
print('您一共用了%d次机会'%i)
'''
#4
'''
row = int(input('请输入你想打印的行数：'))
k=1
while k<=row:
    j=1
    while j<k:
        print(' ',end="")
        j+=1
    i=1
    while i<=2*(row-k)+1 :
        print('*',end='')
        i+=1
    print()
    k+=1
''' 
#5   ????
'''
k = '123'
for i in k:
    print(i)
'''

#6
'''
import random
imax = random.randint(-100,100)
imin = random.randint(-100,100)
c = random.randint(-100,100)
print(imax)
print(imin)
print(c)

if imax < imin:
    t = imin 
    imin = imax
    imax= t
    
if imax < c:
    t = c
    imin = imax
    imax = t  
print("最大的是%d"%imax)
 
if imin > imax:
    imin = imax
elif imin > c:
    imin = c
      
print("最小的是%d"%imin)

'''
#7
'''
'''
#8
'''
item = 0
sum = 0
for item in range(1,101):
    if item % 2 == 0 and item % 7 == 0:
        print(item,end =" ")
        sum+=1
print()
print("一共有%d满足条件"%sum)
'''
'''
#习题一 猜数
import random
sum = 0 
x = random.randint(0,1000)
while 1:
    answer = int(input("请输入一个数："))
    sum+=1
    if answer > x :
        print("大了")
    if answer < x :
        print("小了")
    if answer == x:
        print("You are winner!",'你一共猜了',sum,'次')
        break;
'''

'''
car = 'subaru'
print("Is car == 'subaru'? I predit Ture.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predit False.")
print(car == 'audi')
'''



































































































































































































































































