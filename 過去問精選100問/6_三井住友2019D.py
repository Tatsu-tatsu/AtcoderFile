import itertools
N = int(input())
S = input()
cnt = 0
all = set(itertools.combinations(S, 3))
print(len(all))
# 上記の回答はTLEになる。

# 以下過去自分の書いた模範解答
# 0~9という数字で3桁を出すので全探索している。
# 000~999までしかないというものを全探索している。3桁の数字→最大でも全探索で1000個という判断。
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