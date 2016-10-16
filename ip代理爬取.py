#!/usr/bin/env python
# -*- coding: utf-8 -*-


#settings
ad ='E:/python/newspaper/'

#time
import datetime
now = datetime.datetime.now()
now =  now.strftime('%Y-%m-%d')

#time and name
adress = ad+now+'.txt'

#codeing
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#import
import urllib2,urllib,re,os,lxml
import lxml.etree as etree

#catch html
re1 = urllib2.urlopen("http://www.kuaidaili.com/").read()

#search html
re1 = lxml.etree.HTML(re1)
re2 = re1.xpath('//table[@class="table table-bordered table-striped  table-index"]/tbody/tr/td[@data-title="IP"]|//table[@class="table table-bordered table-striped  table-index"]/tbody/tr/td[@data-title="PORT"]')

# save html
N = 1
for re3 in re2:
    with open(adress,'a') as f:
        f.write(re3.text)
        f.write('\n')

print "finish"
