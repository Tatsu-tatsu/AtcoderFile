N = int(input())
P = list(map(int, input().split()))

people = list(range(1, N+1))
ans = []

for i, p in enumerate(P):
  if i+2 in ans:
    ans.insert(ans.index(i+2)+1, p)
  elif p in ans:
    ans.insert(ans.index(p), i+2)
  else:
    ans.extend([i+2, p])
start = ans.index(1)
finish = ans.index(N)
print(start - finish)

# 解答
## Nから見て1は何世代前か追いかけていく。
## 自分のミス：すべて羅列して、その後出そうとしたが、毎回検索して行うので冗長＆計算量多すぎ。
## 1つずつ戻っていってカウントしていくことが良かった。
N = int(input())
P = list(map(int,input().split()))
ans = 0
while N > 1:
    N = P[N-2]
    ans += 1
print(ans)