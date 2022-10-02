# 幅優先探索
# Point：キューを利用する。キューの存在条件を利用し、深さを記入していく。
import queue
n = int(input())
adj = [[]for i in range(n+1)]
depth = [-1] * (n+1)
for i in range(1, n+1):
  a = list(map(int, input().split()))
  for v in a[2:]:
    adj[i].append(v)

q = queue.Queue()
q.put((1,0)) # 番号、深さ
while(not q.empty()):
    x, d = q.get()
    if depth[x] != -1:
        continue
    depth[x] = d
    for next in adj[x]:
        if depth[next] == -1:
            q.put((next,d+1))

for i in range(1,n+1):
    print(i,depth[i])
