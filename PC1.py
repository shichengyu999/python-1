#!/usr/bin/env python
# -*- coding: utf-8 -*-

#by scy in 10.4-10.6.lt's a practise!

#settings
ad ='E:/python/newspaper/'
sadress = "shichengyu3@126.com"
key ="SGs747700"
tadress = ["shichengyu_@126.com"]

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

#send email
with open(adress,"a+") as d:
    from email.mime.text import MIMEText
    file =d.read()
    #定义邮件内容
    msg = MIMEText(file,"plain","utf-8")
    msg['subject'] = now + '新闻摘要'
    msg['from'] = sadress
    msg['to'] = tadress[0]
import smtplib
server =smtplib.SMTP('smtp.126.com',25)
server.login(sadress,key)
server.sendmail(sadress,tadress,msg.as_string())
server.quit()
print 'all finished!'