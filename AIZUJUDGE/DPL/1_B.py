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

for i in range(N+1):
  dp[i][0] = 0

for i in range(1, N+1):
  for j in range(1, W+1):
    if j - items[i-1][1] >= 0:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j - items[i-1][1]] + items[i-1][0])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[N][W])






