#-*- coding: UTF-8 -*-
# meth1
# myfile = open('data.txt','a+')
# str = myfile.read()
# myfile.close()
# myfile = open('data.txt','a+')
# print str
# myfile.write('aaaaaaaaaaaaaaaaaaaa')
# myfile.close()

# meth2
import os

myfile = open('data.txt','a+')
str = myfile.read()
print str
# 定位指针到末尾
myfile.seek(os.SEEK_END);
myfile.write('aaaaaaaaaaaaaaaaaaaa')
myfile.close()
