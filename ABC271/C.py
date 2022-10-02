import collections 
N = int(input())
a = list(map(int, input().split()))
A = tuple(a)
num = 0
for i in range(N):
  if i+1 in A:
    num += 1
    continue
  else:
    break

ans = 0 + num
for i in range(num, N):
  if a[i] == i+1:
    ans += 1
  else:
    if len(a) - (i+1) >= 2:
      a = a[:-2]
      a.insert(i, i+1)
      ans += 1
    else:
      print(ans)
      exit()
  if len(a) == i+1:
    print(ans)
    exit()

# 一部エラーで解けず。
# 原因：重複するものがあるとき、後ろから消していくと変になること。時間制限。
# 解決策：1.重複問題を対処する。2.検索系はSetを用いて計算量削減。3.dequeを用いて削除の計算量削減。

# 以下模範解答
N = int(input())
A = sorted(list(map(int, input().split())))
# 一意な数値だけを集めるリスト
B = []
# 重複したあまりを集めるリスト
C = []
# 既に現れた数値を記録しておく集合S
S = set()

for a in A:
  if a in S:
    C.append(a)
  else:
    B.append(a)
    S.add(a)
B.extend(C)

# Bを元に両端キューを作る。
D = collections.deque(B)

current = 1
ans = 0

while D:
  if D[0] == current:
    D.popleft()
    ans += 1
    current += 1
  else:
    if len(D) >= 2:
      D.pop()
      D.pop()
      ans += 1
      current += 1
    else:
      break
print(ans)