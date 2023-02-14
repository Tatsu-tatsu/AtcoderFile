# 動的計画法
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())
dp = [0 for _ in range(X+1)]
for b in B:
  dp[b] = 2
dp[0] = 1
# ↓このfor文の回す回数を間違えていたために、時間を使った。
# for文の回す回数、意図を正しく理解する。
for i in range(X):
  if dp[i] == 1:
    for j in range(N):
      if i+A[j] > X or dp[i+A[j]] == 2:
        continue
      dp[i+A[j]] = 1
if dp[X] == 1:
  print("Yes")
else:
  print("No")