n,x = map(int,input().split())
cnt = 0

for i in range(1, n-1):
  for j in range(i+1, n):
    k = x - i - j 
    if k != i and k != j and k <= n and j <= k:
      cnt += 1
print(cnt)

# 初期ミス
## kがjより大きいことを書かなかったので、2倍した値が出てきた。順不同は要注意。