N, T = map(int, input().split())
A = list(map(int, input().split()))
all = sum(A)
rest = T % all
for i in range(N):
  if rest > A[i]:
    rest -= A[i]
  elif rest == A[i]:
    print(i+1, A[i])
    exit()
  elif rest < A[i]:
    print(i+1, rest)
    exit()