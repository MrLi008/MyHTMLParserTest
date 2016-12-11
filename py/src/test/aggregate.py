# coding:utf-8
'''
Created on 2016年12月11日

@author: hasee
test.aggregate
'''



class Aggregate(object):
    def __init__(self, lista=list(), listb=list()):
        self.a = lista
        self.b = listb
        
    '''
    # 交集
    '''
    def intersection(self):
        return [val for val in self.a if val in self.b]
    
    '''
    # 补集
    : if val in a and val not in b
    '''
    def complement_a_b(self):
        return [val for val in self.a if val not in self.b]
    '''
    : if val in b and val not in a
    '''
    def complement_b_a(self):
        return [val for val in self.b if val not in self.a]
    '''
    # 并集
    '''
    def union(self):
        return [val for val in self.intersection() + self.complement_a_b() + self.complement_b_a()]
    
    
'''
# test
'''
if __name__ == '__main__':
    
    test1 = Aggregate([1,2,3,4,5,6], [3,4,5,6,7,8,9])
    
    print test1.intersection()
    print test1.complement_a_b()
    print test1.complement_b_a()
    print test1.union()