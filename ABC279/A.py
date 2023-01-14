S = list(input())
ans = 0
for item in S:
  if item == 'v':
    ans += 1
  if item == 'w':
    ans += 2
print(ans)
