# 動的計画法
# 模範解答
INF = 10 ** 12
N, W = map(int, input().split())

items = [] * N

for i in range(N):
  v, w = map(int, input().split())
  items.append([v, w])

dp = [[INF for i in range(W+1)] for j in range(N+1)]

for i in range(W+1):
  dp[0][i] = 0








