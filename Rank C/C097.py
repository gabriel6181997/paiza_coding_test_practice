# C097: プレゼント応募企画の実施
# https://paiza.jp/challenges/480/show

input_list = list(map(int, input().split()))
N = input_list[0]
X = input_list[1]
Y = input_list[2]
for i in range(N):
    if (i+1) % X == 0 and (i+1) % Y == 0:
        print("AB")
    elif (i+1) % X == 0:
        print("A")
    elif (i+1) % Y == 0:
        print("B")
    else:
        print("N")
