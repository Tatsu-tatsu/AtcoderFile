# データ構造の応用
items = list(input())
nums = []
s = []
ans = 0
for i in range(len(items)):
  if items[i] == '\\':
    nums.append(i)
  elif items[i] == '/' and nums:
    num = nums.pop()
    s_memo = i - num
    while s and s[-1][0] > num:
      s_memo += s.pop()[1]
    # Point：左端を入れることで繋がっているかどうかを判別
    s.append([num, s_memo])
for item in s:
  ans += item[1]
print(ans)
print(len(item[1]), end=' ')
for item in s:
  print(item[1], end=' ')
