# 配列の再生成コストが高いので、作らない方針でTLE→AC
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
one = defaultdict(int)
flag = False
now = 0
for i in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    flag = True
    now = query[1]
    one = defaultdict(int)
  elif query[0] == 2:
    one[query[1]] += query[2]
  elif query[0] == 3:
    if flag:
      print(now + one[query[1]])
    else:
      print(A[query[1]-1] + one[query[1]])
