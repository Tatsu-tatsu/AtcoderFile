A, B, C, X, Y = map(int,input().split())

ans = 10**10

for i in range(10**5+1):
  ans = min(ans, A*max(X-i, 0) + B*max(Y-i, 0) + C*i*2)
print(ans)

# この問題は面倒な半分ずつのピザをiとして計算するとやりやすい。
# Point 何を変数として全探索するとすべてに適応できるかを考える。