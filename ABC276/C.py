import itertools
import copy
N = int(input())
P = list(map(int, input().split()))
for i in range(N-1, -1, -1):
  if P[i] < P[i-1]:
    fix = P[:i-1]
    flg = P[i-1:]
    break
flg_copy = copy.copy(flg)
flg_copy.sort()
index = flg_copy.index(flg[0])
head = flg_copy[index-1]
flg_copy.pop(index-1)
flg_copy.sort(reverse=True)
ans = fix + [head] + flg_copy
print(' '.join(map(str, ans)))