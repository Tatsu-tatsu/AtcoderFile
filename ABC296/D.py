import math
N, M = map(int, input().split())
sqrt_N = int(math.sqrt(N))
sqrt_M = int(math.sqrt(M))
ans = 10**15
for a in range(1, 2*10**6):
  if M % a == 0:
    b = M // a
  else:
    b = M // a + 1
  if a <= N and b <= N:
    if a*b >= M:
      ans = min(ans, a*b)
if N*N == M:
   ans = min(ans, N*N)
if ans == 10**15:
    print(-1)
else:
    print(ans)