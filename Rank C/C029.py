# C029:旅行の計画
# https://paiza.jp/challenges/119/show

data_list = []
weather = []
M, N = list(map(int, input().split()))

for i in range(M):
    data,prob = list(map(int, input().split()))
    data_list.append(data)
    weather.append(prob)

min_prob = 1000
total_prob = None
total_prob_index = None
for i in range(M-N+1):
    total_prob = sum(weather[i:i+N])
    if total_prob < min_prob:
        min_prob = total_prob
        min_prob_index = i

print(data_list[min_prob_index], data_list[min_prob_index+N-1])
