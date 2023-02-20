# 動的計画法：最長共通部分列問題（良問）
n = int(input())
for i in range(n):
  s = input()
  t = input()
  dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
  for i in range(len(t)):
    for j in range(len(s)):
      if t[i] == s[j]:
        dp[i+1][j+1] = dp[i][j] + 1
      else:
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
  print(dp[-1][-1])