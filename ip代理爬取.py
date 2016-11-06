#!/usr/bin/env python
# -*- coding: utf-8 -*-


#settings
ad ='E:/python/newspaper/'

#time
import datetime
now = datetime.datetime.now()
now =  now.strftime('%Y-%m-%d')

#time and name
adress = ad+now+'dl'+'.txt'
adress2 = ad+now+'xw'+'.txt'

#codeing
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#import
import urllib2,urllib,re,os,lxml
import lxml.etree as etree

#catch html
dre1 = urllib2.urlopen("http://www.kuaidaili.com/").read()

#search html
dre1 = lxml.etree.HTML(dre1)
dre2 = dre1.xpath('//table[@class="table table-bordered table-striped  table-index"]/tbody/tr/td[@data-title="IP"]|//table[@class="table table-bordered table-striped  table-index"]/tbody/tr/td[@data-title="PORT"]')

# save html
with open(adress,'w') as f:
    f.write('\n')
N = 1
for dre3 in dre2:
    with open(adress,'a+') as f:
        f.write(dre3.text)
        f.write('\n')
print "finish"

with open(adress,'a+') as f:
    passage1 = f.read()





#top爬虫
#catch html
re1 = urllib2.urlopen("http://top.baidu.com/").read()

#search html
re1 = lxml.etree.HTML(re1)
re2 = re1.xpath('//ul[@id="hot-list"][@class="list"]/*/a[1]')
with open(adress2,'w') as f:
    f.write('\n')
#save hrml
for re3 in re2:
    with open(adress2,'a') as f:
        f.write(re3.text)
        f.write('\n')
    print 'ok'
with open(adress2,'a+') as f:
    passage2 = f.read()


from flask import Flask
app = Flask(__name__)

@app.route('/ip')
def hello_world():
    return  passage1
@app.route('/')
def xw():
    return passage2
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)