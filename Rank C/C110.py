# C110:就職活動
# https://paiza.jp/works/challenges/537/page/result

from collections import defaultdict

N = int(input())

days = []
for _ in range(N):
    days.append(int(input()))

counts = 1

date_and_duration = defaultdict(int)

for i in range(N-1):
    current_day = days[i]
    if current_day + 1 == days[i + 1]:
      counts += 1
    else:
      max_day_index = i + 1 - counts
      duration = counts
      date_and_duration[max_day_index] = duration
      counts = 1

days_index = []
duration_list = []
for key, value in date_and_duration.items():
    days_index.append(key)
    duration_list.append(value)

max_duration_index, max_duration = max(date_and_duration.items(),key=lambda x:x[1])

ans = days[max_duration_index: max_duration_index + max_duration]
print(ans[0], ans[-1])


