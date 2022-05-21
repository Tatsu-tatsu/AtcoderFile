# 以下模範解答
import itertools

N, M = map(int, input().split())

graph = [[0]*N for _ in range(N)]

for i in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1
    graph[b][a] = 1

ans = 0
for num in itertools.permutations(range(N)):
    if num[0] == 0:
        count = 0
        for i in range(N-1):
            if graph[num[i]][num[i+1]] == 1:
                count += 1
        if count == N-1:
            ans += 1

print(ans)

