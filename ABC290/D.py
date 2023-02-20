import math
T = int(input())
for _ in range(T):
  N, D, K = map(int, input().split())
  p = math.gcd(N, D)
  n = N / p
  d = D / p
  ans = (K - 1) // n + ((K-1)*D) % N
  print(int(ans))