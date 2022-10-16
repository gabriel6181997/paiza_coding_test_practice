# C082:【推しプロコラボ問題】テストの赤点
# https://paiza.jp/challenges/397/show

grade_map = {}
E = []
J = []
M = []
X, Y = map(int,input().split())
ans_list = [0]*X
for i in range(X):
  grade_map[i] = list(map(int,input().split()))

for person,score in grade_map.items():
  E.append(score[0])
  J.append(score[1])
  M.append(score[2])

E = sorted(list(E))
J = sorted(list(J))
M = sorted(list(M))

sub = [E,J,M]
for i in range(X):
  for j in range(3):
    if grade_map[i][j] <= sub[j][Y-1]:
      ans_list[i] += 1

for i in ans_list:
  print(i)
