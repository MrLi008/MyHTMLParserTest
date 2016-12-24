# coding:utf-8
'''
Created on 2016年12月24日

@author: hasee

这个其实是在爬安恒的站, 上边有一些安全报告
test.getmessage.spider_simulate.yizhouanquangongtai
'''



import requests
import re
import codecs

url = 'http://www.dbappsecurity.com.cn/safe/safe.html'

data = requests.get(url)

encoding = requests.utils.get_encodings_from_content(data.content)[0]
data.encoding = encoding

print data.text
pattern = r'<a .*href=.*\.pdf'

pattern2 = re.compile(pattern)
print pattern2
match = pattern2.findall(data.text)
# print match
for m in match:
#     print m
    pdf = m.split()[-1]
    print pdf
    nexturl = 'http://www.dbappsecurity.com.cn/safe/' + pdf.split('"')[-1]
    data = requests.get(nexturl)
    data.encoding = encoding
    filepath = pdf.split('/')[-1]
    print filepath
    f = codecs.open(filepath, 'w')
    for chunk in data.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            f.flush()
    f.close()
print 'end......'