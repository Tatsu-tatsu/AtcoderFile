N, P, Q, R, S =map(int,input().split())
A = list(map(int,input().split()))

start = A[0:P-1]
a = A[P-1:Q]
center = A[Q:R-1]
b = A[R-1:S]
end = A[S:N]
ans = start + b+center+a+end
for item in ans:
  print(item, end=' ')