# coding:utf-8
'''
Created on 2016年12月6日

@author: hasee
test.getmessage.httphandle
'''


from HTMLParser import HTMLParser

class MyHTMLParserLocation(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.items = []
        self.flag = False
        
    def handle_starttag(self, tag, attrs):
        
        # 处理标签
        if tag == 'div' and attrs:
            for attr,value in attrs:
                if attr == 'id' and value == 'ip_pos' :
                    # print 'here'
                    self.flag = True
                    return 
        self.flag = False
        
    def handle_data(self, data):
        if self.flag == True:
#             for d in data:
#                 print d
            self.items.append(data)
            
    def show_items(self):
        print 'ip地址解析结果: '
        for item in self.items:
            print item;
            
            
class MyHTMLParserRecordNumber(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recordnumber = ''
        self.flag = False
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and attrs:
            for attr, value in attrs:
                if attr == 'href' and self.issame(value,'www.beian.gov.cn'):
                    # print 'here'
                    self.flag = True
                    return 
#                 self.flag = False
    def handle_endtag(self, tag):
        #self.flag = False;
        pass
                
    def handle_data(self, data):
        if self.flag == True:
            self.recordnumber = data
            self.flag = False
            
            
    def show_record_number(self):
        print '备案号: ',self.recordnumber
        
    def issame(self, value, valuetocompare):
        try:
            hostname = value.split('/')[2]
            # print '解析: ',hostname,'[[[[]]]]',value
            if hostname == valuetocompare:
                return True
        except Exception,e:
            pass
            # print e
            # print '比对失败'
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        