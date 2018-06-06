#-*- coding: UTF-8 -*-
# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# (a>b)?a:b这是条件运算符的基本例子。
score = int(raw_input('please input your mark:'))

if score>=90:
    print 'A'
elif score<90 and score>=60:
    print 'B'
elif score<60 and score>=0:
    print 'C'
else:
    print 'invalid input!'