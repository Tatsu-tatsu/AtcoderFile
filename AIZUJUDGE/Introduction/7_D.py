import numpy as np
n, m, l = map(int, input().split())

A = []
B = []

for i in range(n):
  A.append(list(map(int, input().split())))

for j in range(m):
  B.append(list(map(int, input().split())))

print(A)
print(B)

A2 = np.matrix(A)
print(A2)