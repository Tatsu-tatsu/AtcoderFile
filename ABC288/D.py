N, K = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
  l, r = map(int, input().split())
  items = A[l-1:l-1+r]
  print(items)
  for j in range(1, r):
    num = items[j-1] - items[j]

