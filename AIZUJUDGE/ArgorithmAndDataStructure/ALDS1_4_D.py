# Allocation
# 問題文をよく読む→順番にしか入れれないという記述
# ansとなる最大積載量Pを軸に考えることが重要。大きくしていく中でいつ入り切るか。
# Pが大きくなれば、入る個数は単調増加。→入る個数で2分探索。すべて入るときの場所を探す。
# 詰まったポイント：leftとrightは絶対に当てはまらない値から始める。ex.left = 0
n, k = map(int, input().split())
items = []
for i in range(n):
  items.append(int(input()))

def check(P):
  i = 0
  for j in range(k):
    h = 0
    while (h+items[i]) <= P:
      h += items[i]
      i += 1
      if i == n:
        return True
  return False

left = 0
right = 100000 * 10000
while right - left > 1:
  mid = (right + left) // 2
  if check(mid):
    ans = mid
    right = mid
  else:
    left = mid
print(ans)