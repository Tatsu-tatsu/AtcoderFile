# 以下TLE（for文が4重）
# import collections
# H, W, N, h, w = map(int, input().split())
# items = []
# count_maps = collections.defaultdict(int)

# for i in range(H):
#   a = list(map(int, input().split()))
#   items.append(a)
#   b = collections.Counter(a)
#   for k, v in b.items():
#     count_maps[k] += v
# K = [i for i in range(H - h + 1)]
# L = [i for i in range(W - w + 1)]
# for k in K:
#   for l in L:
#     tmp = 0
#     check = collections.defaultdict(int)
#     for i in range(h):
#       for j in range(w):
#         check[items[i+k][j+l]] += 1
#     for v, z in check.items():
#       val = count_maps[v] - z
#       if val == 0:
#         tmp += 1
#     print(len(count_maps) - tmp, end=' ')
#   print()

# 以下AC
# 毎回初期化するのではなく、愚直に減った分を減らし、増えた分を増やすとfor文が1つ減る。
import collections
H, W, N, h, w = map(int, input().split())
items = []
count_maps = collections.defaultdict(int)

for i in range(H):
  a = list(map(int, input().split()))
  items.append(a)
  b = collections.Counter(a)
  for k, v in b.items():
    count_maps[k] += v
K = [i for i in range(H - h + 1)]
L = [i for i in range(W - w + 1)]

for k in K:
  check = collections.defaultdict(int)
  for i in range(h):
    for j in range(w):
      check[items[k+i][j]] += 1
  for l in L:
    tmp = 0
    if l != 0:
      for i in range(h):
        check[items[k+i][l-1]] -= 1
        check[items[k+i][l+w-1]] += 1
    for v, z in check.items():
      val = count_maps[v] - z
      if val == 0:
        tmp += 1
    print(len(count_maps) - tmp, end=' ')
  print()