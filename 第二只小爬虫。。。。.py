#!/usr/bin/env python
# -*- coding: utf-8 -*-


#这个爬虫可以抓取廖雪峰的Python教程网站上面的所有Python教程，作为看完它写的基础部分的一个小作业吧..工程耗费大概5h左右的时间，正好是开学前一天，开学后编程不会再经常碰了，所以纪念一下
#不过速度感人...抓一个网页要3s左右...
#作者：施程予
#下面的是几个可以更改的变量，根据自己的情况修改，这样也方便以后重复用
#文件的保存根目录
url2 = 'D:/python1/'


#解决编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#根据目录抓取网站的所有链接
import urllib2,urllib,re,requests,os
from bs4 import BeautifulSoup
re1 = urllib2.urlopen('http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000')
re1 = re1.read()

#正则函数
def zz1(wj):
    code1 = str(wj)
    code1 = re.findall(r'<p>(.+)</p>',code1)
    code1 = ''.join(code1)
    code1 = str(code1)
    return code1

#利用正则表达式提取链接
re2 = re.findall(r'<a href="(/wiki/\w{50}|/wiki/\w{50}/\w{50})">',re1) #re2此时是一个dict

#组合url
c = 0
L = []
for re3 in re2:
    url = 'http://www.liaoxuefeng.com'+re3
    L.append(url)


#设定保存网页的函数（用于下面的map） 这个函数是整个爬虫的main函数了，其实做的不是很好，把数据收集，处理和保存都写在了一起，没有再分函数，所以修改这块费了好多好多时间...
def save(url):
    re4 = urllib.urlopen(url)
    re4 = re4.read()

    soup = BeautifulSoup(re4) #创建对象
    re4 = soup.prettify()
    re5 = soup.body
    re5 = re5.find('div',id = 'main').find('div',class_="uk-container x-container")
    re5 = re5.find_all('div',class_="uk-grid")
    re5 = re5[1]
    re5 = re5.find('div',class_="uk-width-1-1").find('div',class_="x-center").find('div',class_="x-content")
    re5 = re5.find('div',class_="x-wiki-content")
    re6 = re5.contents
    re7 = map(zz1,re6)
    b = 7
    global c
    c = c + 1
    while b >= 0 :
        b = b - 1
        a = re7.pop()


    lj = url2+str(c)+'.txt'
    for re8 in re7:
        re8 = re8.decode('utf-8')
        with open(lj,'a') as f:
            f.write(re8)
            f.write('\n')
    return 'ok'


#前面抓到的网站，全部用save函数处理！
K = []
L.pop(49)
for K in L: #前面的都是准备工作，这一行才是真正执行....
    save(K)
    print 'ok!'
    print K


