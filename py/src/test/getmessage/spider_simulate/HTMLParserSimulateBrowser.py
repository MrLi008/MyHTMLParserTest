# coding:utf-8
'''
Created on 2016年12月9日

@author: hasee
test.getmessage.spider_simulate.HTMLParserSimulateBrowser
'''
# coding:utf-8
'''
Created on 2016年12月8日

@author: hasee
test.getmessage.spider_sqlmap.HTMLParserDomainName

description:
    # 提供一个域名
    # 获取该域名下所有网站
    # 获取该域名下所有链接
    # 获取链接中的form表单以及提交方法
    # 生成完整的form表单提交链接并保存
    # 保存格式为:
        # 保存的文件名为域名
        method: [get|post|...]|action: [提交页面]|url: [表单所在页面]
    # 将收集的信息的情况发送email
    
    
    
    # 分析....
        # 添加了线程, 造成了新问题:
        # 过早保存, 未能保存全部链接数据
         
'''
import codecs
from email.mime.text import MIMEText
import smtplib
import threading
from time import sleep



'''
    # form表单标签内不会再有form表单??
    


'''

import requests
from HTMLParser import HTMLParser



# 协议头
headofprotocol = ('http:', 'https:')
webpagetype = ('html', 'jsp', 'asp', 'php', 'aspx', 'com')
links = set()
formdata = dict()

isfinish_scan_all_link = 0


class HTMLParserSimulaterBrower(HTMLParser):
    def __init__(self, domain, protocol, encoding, source_url):
        self.reset()
        
        self.domain = domain
        self.protocol = protocol
        self.encoding = encoding
        self.source_url = source_url
        
        # 取表单:
        self.isform = False
        # 保存form表单的数据
        self.formmethod = ''
        self.formaction = ''
        self.formdata = dict()
        
        
#         print '域名: ', self.domain
#         print '编码: ', self.encoding
        
    def handle_starttag(self, tag, attrs):
#         print 'start: ', attrs
        if tag == 'a' and attrs:
            for (attr, value) in attrs:
                if attr != 'href':
                    break
                try:
                    link = self.is_this_domain_link(self.domain, value)
                except Exception, e:
                    print '判断连接中的域名失败.......', e
                    link = (False,'')
                
                if link[0] == True:
#                     self.links.add(link[1])
#                     print '请求', link[1]
                    mythreadrequests = MyRequestsThread(link[1], self.source_url)
                    mythreadrequests.start()
                    
        elif tag == 'form' and attrs:
#             print 'form......'
            
            attrsdict = dict()
            for attr, value in attrs:
                attrsdict[attr] = value
            try:
                self.formmethod = attrsdict['method']
                self.formaction = attrsdict['action']
            except KeyError,e:
                print '该form标签属性不全:   ',e
            
            self.isform = True
        elif self.isform == True and tag == 'input' and attrs:
            attrsdict = dict()
            
#             print 'formdata ', attrs
            for attr, value in attrs:
                attrsdict[attr] = value
                # 若可获得name属性
#             print 'attrs dict: ', attrsdict   
            
            if attrsdict.has_key('name') and attrsdict.has_key('value'):
                self.formdata[attrsdict['name']] = attrsdict['value']
                
#                 print 'self form data: ', self.formdata
                
                    
    
    def handle_endtag(self, tag):
        if tag == 'form':
            self.isform = False
    
    def handle_data(self, data):
        pass
    
    
    def handle_form(self):
        pass
    
    
            
    
    
    '''
    # 判断获取的连接是否为该域名下的连接
    
    '''
    def is_this_domain_link(self, domain, nexthref):
        
        if nexthref == None:
            return (False, '')
        
        
        flag = False
        fullurl = ''
        
#         print 'domain: ', domain
#         print 'nexthref: ', nexthref
        hrefs = nexthref.split('/')
        urlprotocol = hrefs[0]
       
        # 若连接包含协议头
        if urlprotocol in headofprotocol:
            if hrefs[2] == domain:
                flag = True
#                 fullurl = hrefs[0] + '//' + domain + '/' + hrefs[2:]
                fullurl = nexthref
            else:
                flag = False
            
        # 若连接不包含协议头
        # 以'/' 开头
#         elif hrefs[0] == '':
        else:
            flag= True
            fullurl = self.protocol + '//' + self.domain + '/' + nexthref
            
            
        # 排除js, gif, pag, 等页面
        # 若连接未指向网页
        # 获取页面的类型
        if nexthref.split('?')[0].split('.')[-1] not in webpagetype:
            flag = False
            
#         if type(fullurl) == type(list()):
#             tempfull = fullurl
#             fullurl = ''
#             for t in tempfull:
#                 fullurl = fullurl + t
            
        return (flag, fullurl)
    
    
    
class MyRequests():
    def __init__(self, url, source_url):
        
        self.url = url
        self.source_url = source_url
        
        self.data = ''
        self.encoding = 'utf8'
        
        self.webcontent = ''
        
        self.domain = self.getdomainfrom(self.source_url)
        self.protocol = self.getprotocolfrom(self.source_url)
        
    # 请求并解析网页
    def request(self):
        
        if self.add_new_link(self.url) == False:
#             print '该链接已被添加'
            return
        # 若连接未被访问        
#         print 'request: ', self.url

        headerstr = '''GET/ HTTP/1.1
Host: www.oschina.net
Proxy-Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8'''
        
        
        
        self.data = requests.get(self.url, timeout=300)
        if self.data == None:
#             print '请求未获取数据'
            return
        
        self.encoding = requests.utils.get_encodings_from_content(self.data.content)
        if type(self.encoding) == type(list()) and self.encoding != []:
            self.encoding = self.encoding[0]
        else:
#             print '获取字符编码格式失败'
#             pass
            self.encoding = 'gb2312'
#             return
        
        
        self.data.encoding = self.encoding
        self.webcontent = self.data.text
        
        
#         print 'data: \n\t', self.webcontent, '\n\n---------------->>>>>>>'
        
        hpdn = HTMLParserSimulaterBrower(self.domain, self.protocol, self.encoding, self.source_url)
        
        hpdn.feed(self.webcontent)
        hpdn.close()
        
#         print 'in myrequest, ', hpdn.formdata
        
        self.add_link_form_data(self.url, hpdn)
            
            
        
    
    '''
    # 若链接未被添加, 说明该链接未被访问
    # return:
    #    True for 应访问该链接
    #    False for 该链接已被访问 
    '''
    def add_new_link(self, url):
            
    # 线程锁
        linklock = threading.Lock()
#         print 'prepare.......'
        if linklock.acquire():
#             print 'in lock'
            flag = False
            if url not in links:
                links.add(url)
                flag = True
                
                global isfinish_scan_all_link
                isfinish_scan_all_link += 1
                print isfinish_scan_all_link
            linklock.release()
#             print 'release......'
        
        return flag
        
    
    def add_link_form_data(self, url, httpparserdomainname):
        
        formdatalock = threading.Lock()
        if formdatalock.acquire():
#             print 'in add link from data'
            flag = False
            if formdata.has_key(url) == False:
                formdata[url] = {'formdata':httpparserdomainname.formdata,
                                      'formmethod':httpparserdomainname.formmethod,
                                      'formaction':httpparserdomainname.formaction}
                
                flag = True
                global isfinish_scan_all_link
                print isfinish_scan_all_link
                
                
                isfinish_scan_all_link -=1
                formdatalock.release()
#                 print 'release....'
            
        return flag
        
        
        
    def save_all_links(self):
        try:
            f = codecs.open(self.domain + '.txt', 'a', self.encoding)
    #         for v in sorted(links):
    #             f.write(v)
    #             f.write('\r\n')
            for key in formdata.keys():
                f.write('method: ' + formdata.get(key).get('formmethod') + '|')
                f.write('action: ' + formdata.get(key).get('formaction') + '|')
                f.write('url: ' + key)
                data = formdata.get(key).get('formdata')
                if data != None:
                    fullurl = []
                    for k in data.keys():
                        v = data.get(k)
    #                     f.write(k + '=' + v + '&')
                        fullurl.append( k + '=' + v + '')
                    f.write('?' + '&'.join(fullurl))
                
                f.write('\r\n')
                
            f.close()
        except Exception,e:
            print '保存出了问题......', e
    
    
    
    def show_message(self):
        print '爬取信息: '
        print '\tdomain: ', self.domain
        print '\tlinks: ', 
        self.show_deep(links)
        print '\tform:'
        self.show_deep(formdata)
    
    def show_deep(self, args):
        
        if type(args) == type(tuple()) or type(args) == type(list()):
            for arg in args:
                print arg
#         elif isinstance(args, Iterable) and type(args) != type(''):
        elif type(args) == type(dict()):
            for key in args.keys():
                print key,':{',
                self.show_deep(args.get(key))
                print '}'
        else:
            print args
        
            
    '''
    # 获取url的域名
    '''
    def getdomainfrom(self,url):
        s = url.split('/')
        if s[0] in headofprotocol:
            return s[2]
        return s[0]
    
    def getprotocolfrom(self,url):
        s = url.split('/')
        if s[0] in headofprotocol:
            return s[0]
        return 'http:'
    
    def sendemail(self):
        msg = MIMEText('Hi.....I\'m mrli')
        
        msg['Subject'] = 'don\'t panic'
        msg['from'] = '952934650@qq.com'
        msg['to'] = 'mrli008@ourlook.com'
        
        s = smtplib.SMTP_SSL('smtp.qq.com', timeout=30)
        s.login('952934650@qq.com', '1090 9991 8881 1102')
        
        print s.sendmail('952934650@qq.com', '952934650@qq.com', msg.as_string())
        s.close()
        

        # '109050715@qq.com'
        


class MyRequestsThread(threading.Thread):
    def __init__(self, link, sourceurl):
        threading.Thread.__init__(self)
        self.link = link
        self.sourceurl = sourceurl
            
    def run(self):
        r = MyRequests(self.link, self.sourceurl)
        r.request()
        
        
if __name__ == '__main__':
    
    url = 'http://www.ihs.ac.cn/'
#     url = 'http://www.shanxigov.cn/'
#     url = 'http://blog.csdn.net'
#     url = 'http://www.baidu.com'
#     url = 'http://www.ihs.ac.cn/cp4-3-1.asp'
#     url = 'http://www.qidian.com/'
#     url = 'http://www.jb51.net/'
#     url = 'https://www.douyu.com/'
#     url = 'http://9.fanli.com/'


#     url = 'http://www.oschina.net/'
    
#     url = 'http://seleniumhq.org/'

#     url = 'http://www.51sjyx.com/`'
    
    d = MyRequests(url, url)
    
    
    
    d.request()
    flag = True
    while(flag):
        sleep(2)
#         print 'wait'*20, isfinish_scan_all_link
#         waitlock = threading.Lock()
#         if waitlock.acquire():
        if isfinish_scan_all_link <= 0:
            flag = False
        elif isfinish_scan_all_link <= 10:
            print '这里会比较慢, 请耐心等待'
#             waitlock.release()
        
        
    
    print '*'*80,'\n*save...............'
#     d.show_message()
    d.save_all_links()
#     d.sendemail()
