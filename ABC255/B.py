import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
xy=[]
data = {}
for i in range(N):
  data[i] = []
for i in range(N):
  if i == 0:
    xy.append(list(map(int, input().split())))
    continue
  xy.append(list(map(int, input().split())))
  for j in range(i):
    long = math.sqrt((xy[i][0]-xy[j][0])*(xy[i][0]-xy[j][0]) + (xy[i][1]-xy[j][1])*(xy[i][1]-xy[j][1]))
    data[i].append(long)
print(data)

# 問題文の取り間違え
# 以下模範解答
# Point：表を考えて、最小値を取る。
from math import sqrt
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 番号と一致させるため、面倒な0は埋めておく。
p = [[0,0]]

for i in range(N):
  x, y = map(int, input().split())
  p.append([x,y])

for i in range(K):
  dist = [0]*(N+1)

def CalcDist(a, b):
  return sqrt((p[a][0]-p[b][0])**2 + (p[a][1]-p[b][1])**2)

for Line in range(K):
  for Column in range(1, N+1):
    dist[Line][Column] = CalcDist(A[Line], Column)

ColumnMin = [0]*(N+1)

for Column in range(1,N+1):
  d = 10**10
  for Line in range(K):
    d = min(d, dist[Line][Column])
  ColumnMin[Column]=d

print(max(ColumnMin))