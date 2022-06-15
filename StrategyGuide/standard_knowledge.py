# 行列の計算や扱い方
import numpy as np
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 行列の積
a2 = np.dot(a, a)

# 標準入力が複数行有り、それをすべて文字列として一つで読み取りたい場合
import sys
texts = sys.stdin.read()

# 数字の桁数の処理
N = 2543
n = str(N)
# 配列にする。
n_array = list(map(int, n))
if "3" in n:
  print("3があるよ")
