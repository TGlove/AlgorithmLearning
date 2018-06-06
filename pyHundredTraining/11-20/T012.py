# -*- coding: UTF-8 -*-
# 判断101-200之间有多少个素数，并输出所有素数
cout = 0
for i in range(101, 201):
    if not i % 2 == 0:
        count = 0
        for j in range(1, 201):
            if i % j == 0:
                count += 1
        if count <= 2:
            cout += 1
            print i,
print cout
