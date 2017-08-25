# coding:utf-8
'''
Created on 2016年12月28日

@author: hasee
dataprepare.test_numpy.simple
'''



import numpy as np
from numpy import matlib
from collections import Iterable
# print np
# 
# 
# np.show_config()

# ndarray
# data = [range(10), range(11,20)]
data = list()
for v in range(10):
    data = data + range(v*10)

print data
data2 = np.array(data)
print data2.dtype
print 'ndim: ', data2.ndim
# print 'shape: ', data.shape
# zeros
print np.zeros(10)
print np.zeros((3,6))
print np.ones((3,2,1))

print np.empty((10,20,10))

print np.eye(3)



# dtype
# 通过 指定dtype的值可以 选择数据的读取方式
arr1 = np.array([100000.1111,2000000000.1111,300000000000000.1111],dtype=np.int64)
print arr1
arr1.dtype = np.float64
print arr1

int_array = np.arange(10, dtype=np.int64)
print int_array

calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
print calibers

print int_array.astype(calibers.dtype)
print int_array
int_array.dtype = np.float
print int_array

# 数组的运算
arr = np.array([[1,2,3], [4,5,6]])
print arr
print arr+arr
print arr-arr
print arr*arr
print arr/arr

# numpy array index
# 打印多维数据时, 一行显示的是最低一级的, 一维的数据
# 也就是一行按一维来算
# one dimensional

ary = np.array(range(10))
ary[5:8] = 100
print ary

ary_slice = ary[6:7]
ary_slice[0] = 10
print ary

# two dimensional

ary = np.array([range(10),range(11,20)])
print ary

# print ary[1,2]
ary = np.array([[1,2,3],[4,5,6]])
print ary
print ary[1,2]

ary[0] = 100;
print ary

# more dimensional
ary = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]],[[17,18,19,20],[21,22,23,24]]]);
print ary
ary[:1,:1,:1]=4
print ary

ary = np.ones((4,4,4))
print ary
for v in range(4):
    ary[v,v,v] = 2
print ary

# 正太分布数据
print '正太分布'
normal_distribution = matlib.randn(6,1)
print normal_distribution

str_name = np.array(['Bob','Joe','Will','Bob','Will',
                     'Joe','Joe','Joe'])
# bool_name = 'Bob' == str_name
bool_name = np.ones((8,2))
print 'int8: ',bool_name.astype(dtype=np.int8)
print 'int64: ',bool_name.astype(dtype=np.int64)
# bool_name.dtype = np.bool
print bool_name
print normal_distribution[bool_name.astype(dtype=np.int8)]

print 'another'
 
bool1 = np.ones((3,3, 3))
print bool1
normal_distribution1 = matlib.randn(3, 3)
# bool1.dtype = np.bool
print normal_distribution1
print normal_distribution1[bool1.astype(dtype=np.int8)]
 
# print normal_distribution1*bool1

# Fancy indexing
print 'in Fancy indexing'
arr = np.zeros((3,3,3))
print arr

for i in range(3):
    arr[i%2, i, 2-i] = 1
print arr
'''
# 生成多维数据
# 生成规则:
:input integer n,example n=2
:output  ndarray data_source,example [[0,1],[10,11]] 
'''
def create_data_of_dimen(n):
    
    data_source = list()
    for i in range(n):
        data_source.append(n)
    print data_source
    print 'prepare.....',n,
    d = np.zeros(data_source, dtype=np.int64)
#     print '多维数据\n', d
#     print '遍历:'
    d = show_list(d, n, 0)
    print 'ok'
    return d
def show_list(l, deep, value ):
    if not isinstance(l,Iterable):
#         print l, deep, value
        return value
    else :
        num_col=0
        for v in l:
#             print v, deep, value

            l[num_col] = show_list(v, deep-1, value*10+num_col)
            num_col += 1
        return l
# 被查询维数为n维, 索引为n-1维
d = create_data_of_dimen(4)
print d
# data_source = np.array()
# data_index = np.array([[1],[1]])
data_source = create_data_of_dimen(4)
# data_index = np.ones((7,2))
data_index = np.array([1])
print 'index: \n', data_index.astype(dtype=np.bool)
print 'source: \n', data_source
print 'result: \n',data_source[data_index.astype(dtype=np.int64)]

arr = np.arange(20).reshape((2,10))
print arr.T

print np.dot(arr,arr.T)


arr = create_data_of_dimen(3)
print arr
print arr.T
print arr.swapaxes(1,1,)

# ufunc:
# sqrt, add, maximum, ...
print np.sqrt(arr.astype(dtype=np.double))

points = np.arange(-1,1,0.1)
print points
xs, ys = np.meshgrid(points, points)
print xs,'\n',ys


















