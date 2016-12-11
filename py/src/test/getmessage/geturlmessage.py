# coding:utf-8
'''
Created on 2016年12月6日

@author: hasee
test.getmessage.geturlmessage
'''



import requests
import re
import socket
import codecs
import httphandle






url = raw_input("Please input the url: example: http://www.baidu.com");
# url = 'http://www.ip138.com/'

# hostname
hostname = url.split('/')[2]
print '域名或主机: ', hostname

# ip
thisip = socket.gethostbyname(hostname)
print 'ip: ', thisip


payload = {'s':thisip, 'doit':1}

getlocationdata = requests.post('http://www.ip5.me/index.php', data=payload)
webencode = requests.utils.get_encodings_from_content(getlocationdata.content)
print 'header: ',getlocationdata.headers
getlocationdata.encoding = webencode[0]
# print '网站编码: ', getlocationdata.encoding

data = getlocationdata.text

myhp = httphandle.MyHTMLParserLocation()
myhp.feed(data)

myhp.close()


myhp.show_items()



# 备案号
getlocationdata = requests.get(url)
getlocationdata.encoding = requests.utils.get_encodings_from_content(getlocationdata.content)
data = getlocationdata.text

myhprn = httphandle.MyHTMLParserRecordNumber()
myhprn.feed(data)
myhprn.close()
myhprn.show_record_number()
# save

# 
# req = requests.get(url);
# 
# print req.text;