# 行列の問題はpythonのnumpyというライブラリを使うと楽に計算できる。
# np.array()で多次元配列で計算ができる。

import numpy as np
n, m, l = map(int, input().split())

A = []
B = []

for i in range(n):
  A.append(list(map(int, input().split())))

for j in range(m):
  B.append(list(map(int, input().split())))

C = np.dot(A, B)
for i in range(n):
  for j in range(l):
    print(C[i][j], end="")
  print("")

# 下arrayとmatrixを使った計算方法(matrixは行列に特化したものだが扱いにくいかも)
A2 = np.array(A)
B2 = np.array(B)
# or
A2 = np.matrix(A)
B2 = np.matrix(B)
# ここは行列の掛け算
C = np.dot(A2, B2)
# matrixから配列にもどす。
C2 = np.array(C)
for i in range(n):
  for j in range(l):
    print(C2[i][j], end="")
  print("")