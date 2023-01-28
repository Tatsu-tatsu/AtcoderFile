# パーティション
# 整列の一つ。
n = int(input())
A = list(map(int, input().split()))

def partition(A, p, r):
  x = A[r]
  i = p-1
  for j in range(p, r):
    if A[j] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r], A[i+1]
  return i+1

q = partition(A, 0, n-1)
for i in range(n-1):
  if i == q:
    print("[", end="")
    print(A[i], end="")
    print("]", end=" ")
  else:
    print(A[i], end=" ")
print(A[n-1])
