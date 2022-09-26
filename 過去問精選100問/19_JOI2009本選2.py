import bisect
d = int(input())
n = int(input())
m = int(input())
dx = []
km = []
for _ in range(n-1):
  dx.append(int(input()))
for _ in range(m):
  km.append(int(input()))

dx.append(0)
dx.append(10000000000)
dx.sort()
km.sort()

ans = 0

for k in km:
  index = bisect.bisect_left(dx, k)
  if index == len(dx) - 1:
    if k - dx[index - 1] >= d - k:
      ans += d - k
      continue
    elif k - dx[index - 1] < d - k:
      ans += k - dx[index - 1]
      continue
  if dx[index] - k >= k - dx[index - 1]:
    ans += k - dx[index - 1]
  elif dx[index] - k < k - dx[index - 1]:
    ans += dx[index] - k

print(ans)
# ほぼ正解だが、何かエラー。理解できず。
# 円環は直線にして計算。
# ifではなく、min()で小さい方を足すという式の方がスムーズ
# 大きい数字ではなく、dx.append(d)だと例外処理をせずに対応できそう。
