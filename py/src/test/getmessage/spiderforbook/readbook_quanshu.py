# coding:utf-8
'''
Created on 2016年12月7日

@author: hasee
test.getmessage.spiderforbook.readbook_quanshu
'''
# coding:utf-8
from Cookie import Cookie
'''
Created on 2016年12月7日

@author: hasee
test.getmessage.spiderforbook.HTMLParserBook
'''



from HTMLParser import HTMLParser
import requests
import codecs


'''
example:
    htmlparserbook = HTMLParserBook()
    htmlparserbook.set_novel_url('http://www.baidu.com')
    htmlparserbook.request_url()
    
    htmlparserbook.parser_data()
    
    htmlparserbook.save_message()
    
    
   # 注意事项:
       由于访问不同的小说章节, 从下一章获得的链接不一定完整, 需要手动更改



'''

class HTMLParserBook(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        # 章节数
        self.chapternumber = 0
        
        # 小说名
        self.novelname = ''
        # 小说的章节名, 所在链接, 章节内容
        self.chapternames = list()
        self.chapterlinks = list()
        self.chaptercontents = list()
        
        self.chapternextlink = ''
        
        # 访问到的标签的编号
        self.ischaptername = False
        self.ischapterlink = False
        self.ischaptercontent = False
        
        # 处理符合条件的标签的内容在包含的标签里
        self.incontentdiv = 0
        
        # 访问的小说的连接
        self.url = ''
        self.encoding = ''
        
    def handle_starttag(self, tag, attrs):
        # 链接
        # 设置下一章的链接
        # 收集所有链接
        if tag == 'a' and attrs:
            for (attr, value) in attrs:
                # 获取到下一章的链接
                if attr == 'class' and value == 'next':
                    self.ischapterlink = True
#                     print attrs
                    self.chapternextlink = 'http://www.quanshu.net/book/0/158/' + attrs[0][1]
                    
                    self.chapterlinks.append(self.chapternextlink)
#                     print self.chapternextlink
                    
        # 内容
        elif tag == 'div' and attrs:
            for (attr, value) in attrs:
                if attr == 'id' and value == 'content':
                    self.ischaptercontent = True
#                     print 'in content'
            
            if self.ischaptercontent:
                self.incontentdiv = self.incontentdiv + 1
                    
        # 章节名
        elif tag == 'strong' and attrs:
            for (attr, value) in attrs:
                if attr == 'class' and value == 'l jieqi_title':
                    self.ischaptername = True
        
                            
    def handle_endtag(self, tag):
        if tag == 'div':
            self.incontentdiv = self.incontentdiv - 1
        
            if self.incontentdiv < 1:
                self.ischaptercontent = False
        
                
    def handle_data(self, data):
        if self.ischapterlink:
            # print 'this is chapter link', data
            self.ischapterlink = False
        elif self.ischaptername:
            # print 'this is chapter name', data
            self.chapternames.append(data)
            self.ischaptername = False
            print '获取: ', data
        elif self.ischaptercontent:
            # print 'this is chapter content', data
            self.chaptercontents.append(data.strip())
            
        
        
        
    def set_novel_url(self, url):
        self.url = url
        self.chapternextlink = url
        
        
    def format_url(self, sourceurl, nexturl):
        print sourceurl.split('/').length
        print nexturl.split('/').length 
        newurl = sourceurl[0:-1] + nexturl[0:]
        return newurl
        
        
    '''
    # 获取url请求的内容
    '''
    def request_url(self):
        
#         cook = {'jieqiHistoryBooks':'%5B%7B%22articleid%22%3A%22158%22%2C%22articlename%22%3A%22%u541E%u566C%u661F%u7A7A%22%2C%22chapterid%22%3A%2236641%22%2C%22chaptername%22%3A%22%u7B2C%u4E00%u5377%20%u6DF1%u591C%u89C9%u9192%20%u7B2C%u4E94%u7AE0%20%u4E0D%u540C%u7684%u9009%u62E9%22%7D%5D',
#                 'CNZZDATA1260457973':'1387115548-1481086938-http%253A%252F%252Fwww.quanshu.net%252F%7C1481086938'}
        
        replay = requests.get(self.chapternextlink) #, cookies=cook)
#         print replay
        self.encoding = requests.utils.get_encodings_from_content(replay.content)
#         print self.encoding
        self.encoding = self.encoding[0]
        
#         print '网页编码: ', self.encoding
        replay.encoding = self.encoding
        data = replay.text
        
        return data
        
    def parser_data(self, urldata=''):
        # print 'parser data.....', data
        self.feed(urldata)
        
        '''
        # 将拿到的数据保存
        '''
    def save_message(self):
        try:
            for name in self.chapternames:
                f = codecs.open(u'吞噬星空\\' + name+'.txt', 'w+', self.encoding)
                
                for content in self.chaptercontents:
                    f.write(content)
                f.close()
        except UnicodeEncodeError, e:
            print '保存失败.......',e 
        except IOError, e:
            print e 
    def show_message(self):
        print 'chaptername: '
        for name in self.chapternames:
            print name,' '
        print 'chapterlink: '
        for link in self.chapterlinks:
            print link,' ' 
        print 'chaptercontent: '
        for content in self.chaptercontents:
            print content
        
        
        
if __name__ == '__main__':
    firstchapter = 'http://www.quanshu.net/book/0/158/5141514.html'
    endurl = 'http://www.quanshu.net/book/0/158/index.html'
    
    nextchapter = firstchapter
    
    
    print '开始下载小说: '
    while(nextchapter != endurl):
        h = HTMLParserBook()
        h.set_novel_url(nextchapter)
        data = h.request_url()
        h.parser_data(urldata=data)
        h.save_message()
#         h.show_message()
        nextchapter = h.chapternextlink
    
    print '小说下载完成了, 快去阅读吧........'
    