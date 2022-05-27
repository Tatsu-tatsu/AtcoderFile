# 初期設定をミスったせいで大きく時間をロスした。初期設定が合っているかは確認して進める。
# 以下間違え。indexを毎回使うと探すので計算量でエラーとなる。
N, Q = map(int, input().split())

list = list(range(1, N+1))
for i in range(Q):
  a = int(input())
  if list.index(a) == N-1:
    s = list[N-2]
    t = list[N-1]
    list[N-2] = t
    list[N-1] = s
  else:
    b = list.index(a)
    s = list[b]
    t = list[b+1]
    list[b] = t
    list[b+1] = s

for item in list:
  print(item, end=' ')

# 以下模範解答
# インデックスもデータとして持つ。
## 数字がたくさん出てくるので命名をして、今何の数字について扱ってるか把握する。
## 常にコメントしながら書く。

N, Q = map(int, input().split())
A =list(range(N+1))
idx = list(range(N+1))

for _ in range(Q):
  # xは変更する数字
  x = int(input())
  # インデックス番号を取得
  fi = idx[x]
  if fi != N:
    # 交換先のインデックス番号
    si = fi + 1
  else:
    si = fi - 1
  # yは交換先の数字
  y = A[si]
  A[fi], A[si] = A[si], A[fi]
  idx[x] = si
  idx[y] = fi
