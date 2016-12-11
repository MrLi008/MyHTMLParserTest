# coding:utf-8
'''
Created on 2016年11月27日

@author: hasee
test.excepttest
'''





# 摇色子
import random,os

def init_three_random_number():
    val = (random.randint(1,6), random.randint(1,6),random.randint(1,6));
    return val

while True:
    
    val = init_three_random_number();    
    userinput = input("Please input the number: ");
    userinput = int(userinput);
    
    
    if userinput < sum(val):
        print "too less"
    elif userinput > sum(val):
        print "too bigger"
    else:
        print "you win"
        print val
        break
    
