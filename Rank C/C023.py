# C023:クジの当選番号
# https://paiza.jp/challenges/85/show

answer = []
hit_number = list(map(int, input().split()))
N = int(input())
for i in range(N):
    ticket_bought = list(map(int, input().split()))
    duplicate_list = set(ticket_bought)&set(hit_number)
    answer.append(len(duplicate_list))
for i in answer:
    print(i)
