import itertools

N, M = map(int, input().split())
M_list = []
patterns = []
data = []
max_val = 0
point_data = 0
point = 0
for i in range(M):
  M_list.append(i+1)

for i in itertools.combinations(M_list, 2):
  patterns.append(i)

for i in range(N):
  data.append(list(map(int, input().split())))

for pattern in patterns:
  for i in range(N):
    val = max(data[i][pattern[0]-1], data[i][pattern[1]-1])
    max_val = max(max_val, val)
    point_data += max_val
    max_val = 0
  point = max(point, point_data)
  point_data = 0

print(point)

# 順番に丁寧にやれば問題なし。