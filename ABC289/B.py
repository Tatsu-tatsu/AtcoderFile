N, M = map(int, input().split())
A = list(map(int, input().split()))
A.append(0)
items = [i for i in range(1, N+1)]
ans = []
tmp = []
j=0
for i in range(1, N+1):
  if A[j] == i:
    tmp.insert(0, i)
    j += 1
    continue
  ans.append(i)
  if tmp:
    ans = ans + tmp
    tmp = []
for i in range(N):
  print(ans[i], end=" ")