import math
N = int(input())
places = []
for _ in range(N):
  x, y = map(int, input().split())
  places.append((x, y))
places.sort()
long = 0
for i in range(N):
  for j in range(i, N):
    long += math.sqrt(pow(places[j][0] - places[i][0],2) + pow(places[j][1] - places[i][1],2))
ans = long * 2 / N
print(ans)

# これは計算のダブリが多い。実際に試してみると同じ計算が特定の回数ダブっている。
# したがって、（特定の2つの街の距離の合計）×(2×（N-1）!) / N!
# すなわち（特定の2つの街の距離の合計）× 2 / Nで求まる。
# Point：数学的に簡単に出来ないかは常に考えて実行する。