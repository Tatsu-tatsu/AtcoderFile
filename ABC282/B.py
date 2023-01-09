N, M = map(int, input().split())
data = []
count = 0
ans = 0
for i in range(N):
  S = list(input())
  data.append(S)
for i in range(N):
  for j in range(i+1, N):
    for k in range(M):
      if data[i][k] == 'o' or data[j][k] == 'o':
        count += 1
        continue
      else:
        break
    if count == M:
      ans += 1
    count = 0
print(ans)