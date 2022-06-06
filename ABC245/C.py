from sys import exit
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = []
S.append([A[0], B[0]])
for i in range(N-1):
  for j in range(2):
    if abs(A[i+1]-S[i][j]) and abs(B[i+1]-S[j][j]):
      S.append([A[i], B[i]])
    elif abs(A[i+1]-S[i][j]):
      S.append(A[i])
    elif abs(B[i+1]-S[i][j]):
      S.append(B[i])
    else:
      print("No")
      exit()

if N == len(S):
  print("Yes")

# 上記は失敗。
# 以下模範解答
## ポイント1 2つの可能性が常にあるのでどちらの枝も使いながら進める。（1つに絞りきらない。）
## ポイント2 |= これで、どちらかが論理和を使える。
## ポイント3 動的計画法も可能
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a_ok, b_ok = True, True  # 1個前でA, Bの要素を使うことができるか？
for i in range(N - 1):
    a0, a1 = A[i], A[i + 1]  # 前のA、今のA
    b0, b1 = B[i], B[i + 1]  # 前のB、今のB
    na_ok, nb_ok = False, False  # A[i+1]、B[i+1]を末尾として使えるか？(初期化)
    if a_ok:  # 前の末尾がA[i]にできる場合
        na_ok |= abs(a0 - a1) <= K  # 次の末尾をA[i+1]にできるか判定
        nb_ok |= abs(a0 - b1) <= K  # 次の末尾をB[i+1]にできるか判定
    if b_ok:  # 前の末尾がB[i]にできる場合
        na_ok |= abs(b0 - a1) <= K  # 次の末尾をA[i+1]にできるか判定
        nb_ok |= abs(b0 - b1) <= K  # 次の末尾をB[i+1]にできるか判定
    a_ok, b_ok = na_ok, nb_ok 
if a_ok or b_ok:
  print("Yes")
else:
  print("No")