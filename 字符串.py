# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:47:27 2021

@author: CQ-PRO
"""
# path = 'C:\windows\notepad++.exe'
# print(path)
# path = r'C:\windows\notepad++.exe'
# print(path)

# 在字符串机上r,避免字符串中的字符转义

# x = 999
# so = "%d"%x
# print(so)
# so="%x"%x
# print(so)

# 在 "" 中 加上 %d %i %o %x 转换为 十 十 八 十六

# format()
'''
print('{0:.1f}'.format(1/3))
print('{0:.1%}'.format(1/3))
print('{0:_},{0:_o}'.format(9867569))
# 将数字3位1分,
print('{0:.1},{0:.2}'.format(1/3),'{0:.2f}'.format(1/4))
'''



'''
s= "1,2,3,4,5,6,1"
# !!! 
#这是字符串，不是列表。请注意引号和[] 
print(s.find("6"))
#此时的逗号在字符串中仍作为一个字符，不具有其他意义。故 6 在 10 位 （从0计算）
print(s.count("1"))
# 数 " "  里出现的次数
print(s.split(','))
# 做分割 可以加范围
print(s.replace('6','替换'))
'''

# 查询句子里面的词汇
'''
str_world=input("请输入一句话：")
print(len(str_world.split(" ")))
'''

# str_s=(input(":"))
# print(str_s,'10')

'''
print( '{}'.format(int(input(),16)*2))
'''

'''
str_strip =' assdssa '
print(str_strip)           #原句
print(str_strip.strip(' '))  #将左右两边的“空格” 删去
print(str_strip.lstrip(' a')) #将左边空格删去
print(str_strip.rstrip('a '))  #将右边空格删去
'''

'''
print('Good!'.center(20,"=")) 
# center 语句居中
# ljust  左对齐
# rjust  右对齐
print('abcdefg'[0:4]) 
# 字符串切片，不能对字符串进行修改
'''
 
#!!! 有意思！jieba 

'''
import jieba
x="大家好，我是FC，我来自池州，我想踢足球"
a=jieba.cut(x)
x = jieba.lcut(x)
print(x)
for i in a:
    print(i)
'''


import jieba
txt_1 = "我说话真的不结巴啊，你信不信？"
res = jieba.lcut(txt_1)
#精确模式，返回一个列表类型，其中参数txt是表示文本的名字。吐字清晰版。
print("---吐字清晰版---")
print(res)
res_1 = jieba._lcut_for_search(txt_1)
#搜索引擎模式，返回一个列表类型，其中参数txt是表示文本的名字。吐字结巴版
print("---吐字结巴版---")
print(res_1)
res_2 = jieba.cut(txt_1,cut_all = True)
print("---吐字超级结巴版---")
print(res_2)
#可以看到返回了一个迭代器。<generator object Tokenizer.cut at 0x000001B7D3E28148>
print("---迭代器用循环打开---")
for i in res_2:
    print(i)


# github 学习

# 以三个双引号或单引号开头的字符串可以折行
'''
s1 = """
oh,
ok,
oi
"""
print(s1)
'''


s1 = '\''
print(s1)


# 字符串的小知识
'''
s1 = 'c123456' 
print(s1[2::2])
# print('1' in s1)
if '1' in s1 :
    print('ok')
    # 检查字符串是否由数字构成
    print(s1.isdigit())  # False
    # 检查字符串是否以字母构成
    print(s1.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    print(s1.isalnum())  # True
'''

# 新的print 写法
a,b,c = 1,2,3
print('{0}+{1}*{2}={3}'.format(a,b,c,a+b*c)) 

#3.6格式化字符串还有更为简洁的书写方式
print(f'{a}+{b}={a+b}')  

# 

list1 = [1.099, 3, 15, 7, 100]
print(list1[:len(list1)])
print(sorted(list1))
for index in  list1:
    print(index)

# 
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()

# 元组的使用
list4 = {1,3,2,4,1,1,2,6,7,9,9}
list5 = {1,8,1,3,3,7,8,6,2,6,1}
print(list4 & list5)



# 练习1：在屏幕上显示跑马灯文字。  (interesting)
# !!!
import os
import time

def main():
    content = '北京欢迎你......'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
# if __name__ = '__main__':
main()
    
# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
# !!!
import random 
allchose = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def VerificationCode(allchose,num):
    i = 0
    Code =''
    codeoflen = len(allchose)-1
    while  i < num:
        Code += allchose[random.randint(0,codeoflen)]   
        i+=1
    return Code
print(VerificationCode(allchose,6))    

# 练习3：设计一个函数返回给定文件名的后缀名。

def Suffix(filename,has_dot=False):
    tiger = filename.rfind('.')
    if not has_dot :
        tiger += 1
    print(filename[tiger::])
Suffix('文件.txt') 

# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。

def Max_value(T):
    T.sort()
    list1=[]
    list1.append(T[-1])
    list1.append(T[-2])
    print(list1)
Max_value([12,32,5,5235,535,3523,4,34,2])


# 练习5：计算指定的年月日是这一年的第几天

def now_data(year,moon,day):
    sum = 0
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days[1] = 29
    for i in range(0,moon):
        sum += days[i]
    print(sum+day)
now_data(2020,3, 1)

# 练习6：打印杨辉三角。
#!!!


# 综合案例

# 案例1：双色球选号。

# 综合案例2：约瑟夫环问题。

def LuckyChristian(survivor):
    t,p,i,count = 0,0,0,1
    while p < 15:
        if survivor[t] :
            count += 1
            if count == 9:
                survivor[t] = 0
                count = 1
                p+=1
        i += 1
        t = i%30
    return  survivor        

survivor = [1]*30
survivor = LuckyChristian(survivor)
for sur in survivor:
        print('基' if sur else '非', end='')
# !!!


# 综合案例3：井字棋游戏。
# 抄

import os
def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()


# 练习6.1
def smile(word1,word2):
    for i in range(0,len(word1)):
            for j in range (0,len(word2)):
                if word1[i]== word2[j]:
                    return True                
    return False
smile('quite','ok')

# 练习6.3
def code(coding):
    sum=0
    for i in range(0,len(coding)):
        if not i % 2 == 0:
            sum+=coding[i]*3
        else:
            sum+=coding[i]
    k = 10-sum%10
    
    if k == 10:
        coding.append(0)
    else:
        coding.append(k)
    for i in range(0,len(coding)):
        print(coding[i],end='')
    return coding 
coding =[] 
for i in range(0,13):    
    coding.append(int(input('::')))  
code(coding)       
        
# 练习 6.5
def print_str(html):
    start=html.find('>')
    end =  html.rfind('<') 
    print(html[start+1:end])
if __name__=='__main__':
    print_str(input("请输入html格式："))















