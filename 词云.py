# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 17:29:47 2021

@author: CQ-PRO
"""

import requests
from bs4 import BeautifulSoup
 
for i in range(5):
    allurl='https://movie.douban.com/subject/27010768/reviews?start='+str(i*20)
    res=requests.get(allurl)
    html=res.text
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find('div',class_="article").find('div',class_="review-list").find_all(class_='main-bd')
    for item in items:
        comment_url=item.find('a')['href']
        print(comment_url)



import requests
from bs4 import BeautifulSoup
 
for i in range(5):
    allurl='https://movie.douban.com/subject/27010768/reviews?start='+str(i*20)
    res=requests.get(allurl)
    html=res.text
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find('div',class_="article").find('div',class_="review-list").find_all(class_='main-bd')
    for item in items:
        comment_url=item.find('a')['href']
        #print(comment_url)
        res2=requests.get(comment_url)
        html2=res2.text
        soup2=BeautifulSoup(html2,'html.parser')
        items2=soup2.find('div',class_="article").find('div',id="link-report").find_all('p')
        for item2 in items2:
                print(item2.text)


import requests
from bs4 import BeautifulSoup
comments=open('comments.txt','w+',encoding='utf-8')
 
for i in range(5):
    allurl='https://movie.douban.com/subject/27010768/reviews?start='+str(i*20)
    res=requests.get(allurl)
    html=res.text
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find('div',class_="article").find('div',class_="review-list").find_all(class_='main-bd')
    for item in items:
        comment_url=item.find('a')['href']
        #print(comment_url)
        res2=requests.get(comment_url)
        html2=res2.text
        soup2=BeautifulSoup(html2,'html.parser')
        items2=soup2.find('div',class_="article").find('div',id="link-report").find_all('p')
        for item2 in items2:
                #print(item2.text)
                comments.writelines(item2.text)
comments.close()


import jieba
f=open('comments.txt','r',encoding='UTF-8')
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=' '.join(ls)



import jieba,wordcloud
f=open('comments.txt','r',encoding='UTF-8')
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=' '.join(ls)
w=wordcloud.WordCloud(width=800,height=600,background_color='white',font_path='msyh.ttc',max_words=100)
w.generate(txt)
w.to_file('豆瓣某电影热评.png')






import requests,jieba,wordcloud
from bs4 import BeautifulSoup
comments=open('comments.txt','w+',encoding='utf-8')
 
for i in range(5):
    allurl='https://movie.douban.com/subject/27010768/reviews?start='+str(i*20)
    res=requests.get(allurl)
    html=res.text
    soup=BeautifulSoup(html,'html.parser')
    items=soup.find('div',class_="article").find('div',class_="review-list").find_all(class_='main-bd')
    for item in items:
        comment_url=item.find('a')['href']
        #print(comment_url)
        res2=requests.get(comment_url)
        html2=res2.text
        soup2=BeautifulSoup(html2,'html.parser')
        items2=soup2.find('div',class_="article").find('div',id="link-report").find_all('p')
        for item2 in items2:
                #print(item2.text)
                comments.writelines(item2.text)
comments.close()
f=open('comments.txt','r',encoding='UTF-8')
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=' '.join(ls)
w=wordcloud.WordCloud(width=800,height=600,background_color='white',font_path='msyh.ttc',max_words=100)
w.generate(txt)
w.to_file('豆瓣某电影热评.png')
f.close()















































































