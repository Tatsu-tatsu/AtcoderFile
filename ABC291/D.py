# メモ：998244353この値で割らないとTLEやメモリerrorになる。
# 問題文に余りと書いていたらしっかり割ること。
N = int(input())
A = []
B = []
Mod = 998244353
for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
dp = [[0 for _ in range(2)] for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 1
for i in range(1, N):
  if A[i] != A[i-1]:
    dp[i][0] += dp[i-1][0] % Mod
  if A[i] != B[i-1]:
    dp[i][0] += dp[i-1][1] % Mod
  if B[i] != A[i-1]:
    dp[i][1] += dp[i-1][0] % Mod
  if B[i] != B[i-1]:
    dp[i][1] += dp[i-1][1] % Mod
ans = (dp[N-1][0] + dp[N-1][1]) % Mod
print(ans)