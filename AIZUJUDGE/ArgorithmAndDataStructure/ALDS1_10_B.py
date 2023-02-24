# 連鎖行列積の問題
# 実装はややこしいが、理解はしたので進む。
n = int(input())
p = []
m = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
  a, b = map(int, input().split())
  if i == 0:
    p.append(a)
    p.append(b)
    continue
  p.append(b)

for l in range(2, n+1):
  for i in range(1, n-l+2):
    j = i + l - 1
    m[i][j] = 2**21 #十分大きい数
    for k in range(i, j): # 1つ目の塊の列をkとして計算
      m[i][j] = min(m[i][j], m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j])
print(m[1][n])