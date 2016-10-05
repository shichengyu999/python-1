#!/usr/bin/env python
# -*- coding: utf-8 -*-

#by scy in 10.4.lt's a practise!

#解决编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')   #finish code problme

#导入变量
import urllib2,urllib,re,os,lxml
import lxml.etree as etree

#catch html
re1 = urllib2.urlopen("http://top.baidu.com/").read()
print re1



re1 = lxml.etree.HTML(re1)
print re1
re2 = re1.xpath('/html/body/div[@class="wrappr"]/div[@id="main"]/div[@class="row"][1]/div[@class="box-hot tab"]/div[@class="tab-bd"]/div[@class="tab-box"]/ul')
print re2


