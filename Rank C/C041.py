# C041:メダルランキングの作成
# https://paiza.jp/challenges/185/show

N = input()
country_medal = {}
gold = []
silver = []
bronze = []
country = [0]*N
for i in range(N):
  country_medal[i] = list(map(int,input().split()))

for country,medal in country_medal.items():
  gold.append(medal[0])
  silver.append(medal[1])
  bronze.append(medal[2])
