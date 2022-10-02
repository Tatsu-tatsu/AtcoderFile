# 以下自力回答
# Point：幅優先探索は、キューを定義。深さとなるものを定義。キューが無くなるまで実行。
import queue
R, C = map(int, input().split())
s = list(map(int, input().split()))
g = list(map(int, input().split()))
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

c = []
for i in range(R):
  c_list = list(input())
  c.append(c_list)
depth = [[-1]*C for _ in range(R) ]
q = queue.Queue()
q.put((s[1]-1, s[0]-1, 0))
while(not q.empty()): # ここはポイント。
    x, y, d = q.get()
    if depth[y][x] != -1:
      continue
    depth[y][x] = d
    for dx, dy in dxdy:
      if c[y+dy][x+dx] == ".":
        q.put((x+dx, y+dy, d+1))

print(depth[g[0]-1][g[1]-1])