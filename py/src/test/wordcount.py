#-*-coding:utf-8-*-
'''
Created on 2016年11月28日

@author: hasee
test.wordcount
'''

# import codecs
def myhash(values):
    value = 0;
    index = 1;
    for v in values:
        if type(v) == type(list()):
            value = value + myhash(v);
        elif type(v) == type(dict()):
            value = value + myhash(dict);
        else:
            value = value + ord(v) * index;
            index = index*10;
    return value;

#dict
counter = {}
# egm = open("Walden.txt", 'r');
egm = open("test_wordcount.txt", 'r+');

for word in egm.read().split():
    print word,myhash(word);
    wordhash = myhash(word);
    if counter.has_key(wordhash) == False:
        counter[wordhash] = 0;
    counter[wordhash] = counter[wordhash] + 1;
    
egm.close();

Walden = 1
print counter;
print type(counter.get(19401));

strcounted = raw_input('input the word to be counted: ');
# strcounted = strcounted.encode('utf-8')
hashcounted = myhash(strcounted);
print hashcounted, type(hashcounted);
if counter.has_key(hashcounted):
    print 'the count: ', counter.get(hashcounted)
else:
    print 'no this word'

# open file
# input countered word
# read file
# compare
# close file






