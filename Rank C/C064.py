# C064: paizaでお食事
# https://paiza.jp/challenges/312/show

from collections import defaultdict
import math

M, N = map(int,input().split())

menu_cal = []
eaten_amount = defaultdict(int)

for _ in range(M):
    menu_cal.append(int(input()))

for i in range(N):
    eaten_amount[i] = list(map(int,input().split()))

for key, value in eaten_amount.items():
    eaten_amount[key] = list(map(lambda x:x/100, value))

ans = []
for cal_list in eaten_amount.values():
   total_cal = 0
   for cal, amount in zip(menu_cal, cal_list):
       total_cal += math.floor(cal * amount)
   ans.append(total_cal)

for cal in ans:
    print(cal)

