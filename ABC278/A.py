N, K = map(int, input().split())
A = list(map(int, input().split()))
if N < K:
  ans = A[K:] + [0]*N
else:
  ans = A[K:] + [0]*K
for a in ans:
  print(a, end=' ')