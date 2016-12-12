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
        url = '网站url链接'
        tags = 
        {
            'tagName1':
            {
                ('attrName1':'attrValue1'),
                ('attrName2':'attrValue2')
            }
            'tagName2':
            {
                ('attrName3':'attrValue3'),
                ('attrName4':'attrValue4'),
            }
        }
    
    # 要得到的数据
        : 网站的所有链接
        : 网站上的图片, 资源
        : 网站上标签内包含的所有文本
        : ........




    # 实现框架:
    # 面向单个页面, 只针对当前页面
        # 使用HTMLParser类解析网页文档
        # 主要用到的函数:
            : In HTMLParse
            : handle_starttag(self, tag, attrs)
                : tag: 标签名
                : attrs:# 原本是[(attrname,attrvalue),(attrname,attrvalue)]
                        # 我决定要改成: {'attrname':'attrvalue','attrname1':attrvalue'}
                        : 添加一个转换函数 changetodictof(attrs) return dict{}
                        # 由于用户输入若设为字典类型, HTMLParser也需要转换attrs为字典,
                        # 不如设用户输入与attrs为同一类型. 另建类aggregate实现集合的交并补
            : handle_endtag(self, tag)
            : handle_data(self, data)
            
            
            
            
    # 作为判断的依据
        1, 标签
            1.1, 以该标签开始, 以该标签结束, 收集这之间的所有数据
                1.1.1, 标签的属性
                    : 是否有某个属性
                    : if tags.has_key(tag):
                    :    userattrs = tags.get(tag)
                    :    # 若userattrs对于attrs的补集为空, 说明该标签符合查找条件
                    :    if aggregate(userattrs, attrs).complement_a_b() == []:
                    :        # 找到符合条件的标签
                1.1.2, 标签的属性的值
                    : 
                    : if tags.has_key(tag):
                    :    userattrs = tags.get(tag) # 获取用户输入的标签的属性{'attrname':'attrvalue'}
                    :    websiteattrs = changetodictof(attrs)
                1.1.3, 标签的文本数据
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
    
    print '集合操作: '
    list1 = [1,2,3,4,5,6,7]
    list2 = [5,6,7,8,9,0]
    print [val for val in list1 if val in list2]
    print [val for val in list1 if val not in list2]
    print [val for val in list2 if val not in list1]
    print [val for val in [val for val in list1 if val in list2] + [val for val in list1 if val not in list2] + [val for val in list2 if val not in list1]]
    val = set()
    for v in list1:
        val.add(v)
    for v in list2:
        val.add(v)
    print val
    
    
    
    
    
