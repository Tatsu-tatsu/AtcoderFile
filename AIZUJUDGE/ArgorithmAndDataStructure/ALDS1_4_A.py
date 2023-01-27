# 線形探索
# メモ：計算量が間に合うので、何も気にせずfor文回すだけ。
n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

count = 0
S.sort()
T.sort()
for t in T:
  for s in S:
    if s == t:
      count += 1
      break
print(count)

# 番兵法：比較回数を減らすことで少し高速にできる。ただしデータ数が多い場合のみ。
# 配列の最後に該当する値を入れることで確実に終わらせれる。
# for文のfor(i=0; i < n: i++)における比較演算の回数減らせることがメリットなので、Pythonでは効果が無い可能性もある？

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
count = 0

for t in T:
  i = 0
  S.append(t)
  while t != S[i]:
    i += 1
  if i != len(S) - 1:
    count += 1
print(count)