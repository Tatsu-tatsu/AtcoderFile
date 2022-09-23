# 以下模範解答
# 右回り限定にして、2点から存在するかどうかを検討し、あれば面積を出す。
# Point:2点を組み合わせで選び、右回りに絞ることを限定して全探索したこと
from itertools import combinations
N = int(input())
dots = []
for i in range(N):
  x, y = map(int, input().split())
  dots.append((x, y))
dots.sort()
ans = 0
for p1, p2 in combinations(dots, 2):
  x1, y1 = p1
  x2, y2 = p2
  if (x2 + y2 - y1, y2 + x1 - x2) in dots and (x1 + y2 - y1, y1 + x1 - x2) in dots:
    ans = max(ans, (x1 - x2)**2 + (y1 - y2)**2)
print(ans)