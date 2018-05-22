#-*- coding: UTF-8 -*-

# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，
# 可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，
# 可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# profit = float(raw_input('please input your profit this month : '))
#
# bonus = 0
# rate = [0.1,0.075,0.05,0.03,0.015,0.01]
# l = [0,100000,200000,400000,600000,1000000]
# for i in range(5):
#     if profit<l[i]:
#         if i ==1:
#             bonus = profit * rate[0]
#             break
#         else:
#             for j in range(i-1):
#                 bonus += (l[j+1]-l[j])*rate[j]
#             bonus += (profit - l[i-1])*rate[i-1]
#             break
#     else:
#         bonus = 39500 + (profit-1000000)*0.01
# print bonus

i = int(raw_input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print (i-arr[idx])*rat[idx]
        i=arr[idx]
print r