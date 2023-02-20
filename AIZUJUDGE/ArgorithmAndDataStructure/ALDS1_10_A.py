# メモ化再帰
def fib(n):
  if n == 0 or n == 1:
    F[n] = 1
    return F[n]
  if F[n] != None:
    return F[n]
  F[n] = fib(n-1) + fib(n-2)
  return F[n]

N = int(input())
F = [None] * (N+1)
fib(N)
print(F[N])