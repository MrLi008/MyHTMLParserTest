# coding:utf-8
'''
Created on 2016年12月9日

@author: hasee
test.getmessage.spider_simulate.HTMLParserSimulateAndroid
'''
# 
# from selenium import webdriver
# 
# 
# a = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.ANDROID)
# print a.get('http://www.baidu.com')

'''


    # 传入的数据的结构:
        tags = 
        {
            'tagName1':
                {
                    'attrName1':'attrValue1',
                    'attrName2':'attrValue2'...
                }
            'tagName2':
                {
                    'attrName3':'attrValue3',
                    'attrName4':'attrValue4'...
                }
        }


    # 实现框架:
        # 使用HTMLParser类解析网页文档
        # 主要用到的函数:
            : handle_starttag(self, tag, attrs)
            : handle_endtag(self, tag)
            : handle_data(self, data)
    # 作为判断的依据
        1, 标签
            1.1, 以该标签开始, 以该标签结束, 收集这之间的所有数据
                1.1.1, 标签的属性及值, 
                                : if tags.has_key(tag):
                                :    attrs = tags.get(tag) # 获取
                                :    
                1.1.2, 标签的文本数据
            1.2, 以该标签开始, 到该标签结束, 只收集该标间相关的数据
            1.3, 收集某标签内的某标签内的某标签....标签的数据
        2, 属性
        3, 属性值
    # 获得的数据
        1, 网页内容
    # 保留的数据
        1, 某标签的某个属性
        2, 某标签的数据(data)
        3, 如果某个标签内还有标签的解决办法
        
    # 经验:
        1, 如果能避免使用递归, 就避免....
        2, 尝试使用线程加快解析速度
        3, 
'''



class TestAttrDict(object):
    def __init__(self, tuple_tag_name_value=()):
        
        self.dict=dict()
        
        for (attr, value) in tuple_tag_name_value:
            self.dict[attr] = value
            
            
    def show_message(self):
        print self.dict
        
if __name__ == '__main__':
    
    themap = [('attr1', 'value1'), ('attr2', 'value2')]
    
    
    t = TestAttrDict(themap)
    
    t.show_message()
    
    
    ll= [1,2,3,4,5]
    print ll[1:-1]
    print ll[1:2]
    print ll[-1:0]
    print ll[0:-1]
    print ll[-2:-1]
    ll = [0, 1]
    print ll[0:-1]
