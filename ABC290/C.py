N, K = map(int, input().split())
A = list(map(int, input().split()))
B = set(A)
ans = 0
for i in range(K):
  if i in B:
    ans += 1
  else:
    break
print(ans)