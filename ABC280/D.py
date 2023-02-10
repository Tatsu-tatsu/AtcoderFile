# メモ：素因数分解をする計算量が大きい。1回だけにしたい。
def prime_factorize(N):
    res = []
    for p in range(2, N):
        if p * p > N:
            break
        if N % p != 0:
            continue
        e = 0
        while N % p == 0:
            e += 1
            N //= p
        res.append((p, e))

    if N != 1:
        res.append((N, 1))

    return res

K = int(input())
X = prime_factorize(K)
ans = 0
for x, num in X:
  res = num
  for Nx in range(x, x*(num+1), x):
    j = Nx
    while j % x == 0:
      j = j / x
      res -= 1
      if res <= 0:
        break
    if res <= 0:
      ans = max(ans, Nx)
      break
print(ans)