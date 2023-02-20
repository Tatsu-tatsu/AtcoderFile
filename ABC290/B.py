N, K = map(int, input().split())
S = input()
count = 0
ans = []
for i in range(N):
  if count == K:
    ans.append('x')
    continue
  if S[i] == 'o':
    count += 1
    ans.append('o')
  else:
    ans.append('x')
print(''.join(ans))