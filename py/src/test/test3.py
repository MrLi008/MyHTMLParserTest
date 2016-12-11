# coding:utf-8
'''
Created on 2016年11月26日

@author: hasee
test.test3
'''
import os

print os.listdir("D:\\");
deep = 1;

def loadfiles(updir, deep):
    try:
        listoffile = os.listdir(updir);
    except Exception, e:
        print "wrong!!", e;
        return
    
    for f in listoffile:
        print "-"*deep+">", os.path.abspath(f)
        if os.path.isfile(f):
            pass;
        else:
            loadfiles(updir+"\\"+f, deep+1);
            
loadfiles("..\..", deep);

# os.command
print os.system("dir");


