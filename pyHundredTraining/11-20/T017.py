#-*- coding: UTF-8 -*-
# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
str = raw_input('please input whatever you want: ')
sum_litter = 0
sum_space = 0
sum_number = 0
sum_others = 0
for i in range(len(str)):
    if str[i].isspace():
        sum_space +=1
    elif str[i].isdigit():
        sum_number +=1
    elif str[i].isalpha():
        sum_litter +=1
    else:
        sum_others +=1
print 'space=',sum_space, 'litter=',sum_litter ,'number=',sum_number ,'others =',sum_others