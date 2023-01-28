N, M = map(int, input().split())
S = []
T = []
for i in range(N):
  item = str(input())
  tips = item[3:6]
  S.append(int(tips))
for j in range(M):
  item = int(input())
  T.append(item)
count = 0
for s in S:
  for t in T:
    if s == t:
      count += 1
      break
print(count)
