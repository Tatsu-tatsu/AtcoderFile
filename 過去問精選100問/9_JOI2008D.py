m = int(input())
star = []
for _ in range(m):
  x, y = map(int, input().split())
  star.append((x, y))
n = int(input())
list = []
for _ in range(n):
  X, Y = map(int, input().split())
  list.append((X, Y))
base = star[0]
cnt = 0
for listItem in list:
  cnt = 0
  sx = listItem[0] - base[0]
  sy = listItem[1] - base[1]
  for starItem in star:
    if (starItem[0] + sx, starItem[1] + sy) in list:
      cnt += 1
    else:
      break
    if (cnt == m):
      print(sx, sy)
      exit()
# Point：基準となる1つの星を決めて全探索すれば全通り出てくる。計算量はmnなので余裕。