# coding:utf-8
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
                if attr == 'id' and value == 'j_chapterNext':
                    self.ischapterlink = True
                    
                    self.chapternextlink = 'http:' + attrs[1][1]
                    
                    self.chapterlinks.append(self.chapternextlink)
                    print self.chapternextlink
                    
        # 内容
        elif tag == 'div' and attrs:
            for (attr, value) in attrs:
                if attr == 'class' and value == 'read-content j_readContent':
                    self.ischaptercontent = True
                    # print 'in content'
                    
        # 章节名
        elif tag == 'h3' and attrs:
            for (attr, value) in attrs:
                if attr == 'class' and value == 'j_chapterName':
                    self.ischaptername = True
        
                    
    def handle_endtag(self, tag):
        if tag == 'div':
            self.ischaptercontent = False
        
                
    def handle_data(self, data):
        if self.ischapterlink:
            # print 'this is chapter link', data
            self.ischapterlink = False
        elif self.ischaptername:
            # print 'this is chapter name', data
            self.chapternames.append(data)
            self.ischaptername = False
        elif self.ischaptercontent:
            # print 'this is chapter content', data
            self.chaptercontents.append(data.strip())
            
        
    def set_novel_url(self, url):
        self.url = url
        self.chapternextlink = url
        
        '''
        # 获取url请求的内容
        '''
    def request_url(self):
        
        replay = requests.get(self.chapternextlink)
        self.encoding = requests.utils.get_encodings_from_content(replay.content)[0]
        
        print '网页编码: ', self.encoding
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
        
        for name in self.chapternames:
            f = codecs.open(u'主神大道\\' + name+'.txt', 'w+', self.encoding)
            
            for content in self.chaptercontents:
                f.write(content)
            f.close()
    
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
    #while(nextchapter != ''):
    h = HTMLParserBook()
    h.set_novel_url(nextchapter)
    data = h.request_url()
    print data
    #h.parser_data(urldata=data)
    h.save_message()
    # h.show_message()
    nextchapter = h.chapternextlink

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    