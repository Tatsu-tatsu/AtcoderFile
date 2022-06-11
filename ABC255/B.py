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
