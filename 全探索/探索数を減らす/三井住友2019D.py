# 模範解答
N = int(input())
S = input()

result = 0
for i in range(10):
  a = S.find(str(i))
  if a == -1:
    continue
  for j in range(10):
    b = S.find(str(j), a + 1)
    if b == -1:
      continue
    for k in range(10):
      c = S.find(str(k), b + 1)
      if c != -1:
        result += 1

print(result)

# 計算量を減らした別解
## 3文字以上は必要ないのでSを新しくTに置き換える。

N = int(input())
S = input()

t = [S[0]]
p = S[0]
r = 1
for i in range(1, N):
    if S[i] == p:
        r += 1
        if r < 4:
            t.append(S[i])
    else:
        r = 1
        t.append(S[i])
# ここで配列tをすべて結合させて文字列Tに変換する。
T = ''.join(t)

result = 0
for i in range(10):
    a = T.find(str(i))
    if a == -1:
        continue
    for j in range(10):
        b = T.find(str(j), a + 1)
        if b == -1:
            continue
        for k in range(10):
            if T.find(str(k), b + 1) != -1:
                result += 1
print(result)