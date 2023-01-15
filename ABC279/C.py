# メモ：深さ優先探索な気がしている。
# 計算量を概算して、不可能であれば違う選択肢をコードを書く前に行うべき。
H, W = map(int, input().split())
S = []
T = []
count = 0
for i in range(H):
  S.append(list(input()))
for i in range(H):
  T.append(list(input()))
ans = [False] * W
# 横列
for i in range(W):
  count = 0
  # 縦列
  for j in range(H):
    if S[i][j] == T[i][j]:
      count += 1
    else:
      break
    if count == H:
      ans[i] = True
      S.pop()

# ans
# 列で決めたいので列でsortする。
H, W = map(int, input().split())
S = [[] for _ in range(W)]
T = [[] for _ in range(W)]
for i in range(H):
  row = list(input())
  for j in range(W):
    S[j].append(row[j])
for i in range(H):
  row = list(input())
  for j in range(W):
    T[j].append(row[j])
newS = sorted(S)
newT = sorted(T)
if newS == newT:
  print("Yes")
else:
  print("No")