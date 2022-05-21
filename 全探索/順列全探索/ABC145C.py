# 以下模範解答
from math import sqrt
N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

result = 0
for i in range(N):
  for j in range(N):
    if i != j:
      result += sqrt((l[i][0] - l[j][0])**2 + (l[i][1] - l[j][1])**2)

print(result / N)