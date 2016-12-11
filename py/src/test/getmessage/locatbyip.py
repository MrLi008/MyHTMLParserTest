# coding:utf-8
'''
Created on 2016年12月6日

@author: hasee
test.getmessage.locatbyip
'''


import socket, requests
import httphandle
import re

class WebSiteMessage(object):
    def __init__(self):
        self.hostname = ''
        self.ip = ''
        self.encodings = ''
        
        # initialize the post data
        self.payload = {'doit':1}
        
        '''
        url应包含协议头
        '''
    def gethostname(self, url):
        try:
            self.hostname = url.split('/')[2]
        except Exception,e:
            print '解析url出错, 获取主机名或域名失败..', e
        
        return self.hostname
    
    
    def getip(self, url):
        try:
            self.gethostname(url)
            self.ip = socket.gethostbyname(self.hostname)
        except Exception,e:
            print '解析url出错, 获取ip失败..', e
            
    
    '''
            获取位置信息
    '''
    def get_location_data(self, url):
        
        self.payload['s'] = self.getip(url)
        # post requests
        locationdata = requests.post('http://www.ip5.me/index.php', data=self.payload)
        
        print '访问ip地址查询网站: ',locationdata.status_code
        # set encoding
        
        self.encodings = requests.utils.get_encodings_from_content(locationdata.content)[0]
        
        locationdata.encoding = self.encodings
        
        # analysis
        data = locationdata.text
        
        myhpl = httphandle.MyHTMLParserLocation()
        myhpl.feed(data)
        myhpl.close()
#         myhpl.show_items()
        
        return myhpl.items[0]
    
    '''
    获取备案信息
    '''
    def get_record_number(self, url):
        getlocationdata = requests.get(url)
        self.encodings = requests.utils.get_encodings_from_content(getlocationdata.content)[0]
        getlocationdata.encoding = self.encodings
        data = getlocationdata.text

        myhprn = httphandle.MyHTMLParserRecordNumber()
        myhprn.feed(data)
        myhprn.close()
        return myhprn.recordnumber
    
    def show_record_number(self,url):
        recordnumber = self.get_record_number(url)
        # 正则解析
#         rec = u'([/u4e00-/u9fa5])'
#         parttern = re.compile(rec)
#         res = parttern.findall(recordnumber)
#         
#         
#         print rec
        print '备案号为: ', recordnumber
    
    def show_address(self, url):
        location = self.get_location_data(url)
        print 'IP地址解析结果: ', location


if __name__ == '__main__':
    test = WebSiteMessage()
#     str = 'http://nuomi.baidu.com/'
    str = 'http://www.panc.cc/'
    test.show_address(str)
    test.show_record_number(str)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        