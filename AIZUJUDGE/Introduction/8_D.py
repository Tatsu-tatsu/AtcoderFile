# 問題読み間違え。以下ミス。
s = input()
p = input()

cnt = 0

for i in p:
  if i in s:
    cnt += 1

if cnt == len(p):
  print(cnt)
  print(len(p))
  print("Yes")
elif cnt != len(p):
  print("No")

# 以下模範解答
# Point1:円を描く文字列は、s*2で文字列を2つ繋げて考える。
# Point2:（p in s）のように文字列の中に文字列が存在しているとき、trueとなる検索方法。
s = input()
p = input()

s = s * 2

if p in s:
  print('Yes')
else:
  print('No')