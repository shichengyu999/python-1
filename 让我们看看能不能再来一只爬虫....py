#!/usr/bin/env python
# -*- coding: utf-8 -*-

#by scy in 10.4.lt's a practise!

#settings
ad ='E:/python/newspaper/'

#codeing
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#time
import datetime
now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d')

#time and name
adress = ad+now+'.txt'

#import
import urllib2,urllib,re,os,lxml
import lxml.etree as etree

#catch html
re1 = urllib2.urlopen("http://top.baidu.com/").read()

#search html
re1 = lxml.etree.HTML(re1)
re2 = re1.xpath('//ul[@id="hot-list"][@class="list"]/*/a[1]')

#save hrml
for re3 in re2:
    with open(adress,'a') as f:
        f.write(re3.text)
        f.write('\n')
    print 'ok'

