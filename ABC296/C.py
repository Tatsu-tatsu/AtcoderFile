import collections
N, X = map(int, input().split())
A = list(map(int, input().split()))
c = collections.Counter(A)
for k, v in c.items():
  num = k + X
  if num in c:
    print("Yes")
    exit()
print("No")