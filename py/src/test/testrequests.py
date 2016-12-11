# coding:utf-8
'''
Created on 2016年11月28日

@author: hasee
test.testrequests
'''
import requests

r = requests.get(url='http://wingware.com/pub/wingide/5.1.12/wingide-5.1.12-1-x86_64-linux.tar.gz');
print r.status_code;

# r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'});

print r.url
print r.encoding
# print r.text.encode('utf-8')

f = open("wingide-5.1.12-1-x86_64-linux.tar.gz", 'w+');
f.write(r.text);
f.close();