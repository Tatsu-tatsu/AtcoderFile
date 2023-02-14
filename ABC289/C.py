import itertools

N, M = map(int, input().split())
ans = 0
items = []
for i in range(M):
  c = int(input())
  a = set(map(int, input().split()))
  filter(lambda x: x <= N, a)
  items.append(a)
comb = []
for i in range(1, M+1):
  com = list(itertools.combinations(items, i))
  comb += com
for i in range(len(comb)):
  com = comb[i]
  check = set()
  for j in range(len(com)):
    check = check | com[j]
  if len(check) == N:
    ans += 1
print(ans)