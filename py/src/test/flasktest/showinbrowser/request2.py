# coding:utf-8
'''
Created on 2016年12月21日

@author: hasee
test.flasktest.showinbrowser.request2
'''

import requests

payload = {'username':'\'','password':'1'}
url = 'http://web1112.int0x80.in/login.php'
req = requests.post(url, data=payload)

print req

thisencoding = requests.utils.get_encodings_from_content(req.content)[0]
req.encoding = thisencoding

print req.text