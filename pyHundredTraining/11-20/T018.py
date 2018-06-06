# -*- coding: UTF-8 -*-
# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
a = raw_input('a= ')
n = int(raw_input('n= '))
result = a
suma = int(a)
for i in range(n-1):
    result += a
    suma += int(result)
print suma