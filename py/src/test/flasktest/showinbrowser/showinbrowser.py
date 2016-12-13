# coding:utf-8
'''
Created on 2016年12月13日

@author: hasee
test.flasktest.showinbrowser.showinbrowser
'''

from flask import Flask
app = Flask(__name__)

@app.route('/<usr>')
def h(usr):
    return 'Hi, %s' % usr

if __name__ == '__main__':
    app.run()