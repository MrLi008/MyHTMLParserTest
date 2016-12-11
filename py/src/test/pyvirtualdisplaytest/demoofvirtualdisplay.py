# coding:utf-8
'''
Created on 2016年12月9日

@author: hasee
test.pyvirtualdisplaytest.demoofvirtualdisplay
'''
from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay
with SmartDisplay(visible=0, bgcolor='black') as disp:
    with EasyProcess('xmessage hello'):
        img = disp.waitgrab()
img.show()