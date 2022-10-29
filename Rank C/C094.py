# C094: 国民の税金
# https://paiza.jp/works/challenges/461/page/result

import math

N = int(input())
all_taxes = []
for i in range(N):
  tax = 0
  money = int(input())
  if 0 <= money <= 100000:
    tax = 0
  elif 100001 <= money <= 750000:
    tax = (money - 100000) * 0.1
  elif 750001 <= money <= 1500000:
    tax = 650000 * 0.1 + (money - 750000) * 0.2
  else:
    tax = 650000 * 0.1 + 750000 * 0.2 + (money - 1500000) * 0.4
  all_taxes.append(math.floor(tax))
ans = sum(all_taxes)
print(ans)
