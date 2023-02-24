n = int(input())
ans = [[0] * n for _ in range(n)]
for i in range(n):
  items = list(map(int, input().split()))
  u = items[0]
  k = items[1]
  for j in range(k):
    ans[u-1][items[j+2]-1] = 1
for i in range(n):
  print(' '.join(map(str, ans[i])))