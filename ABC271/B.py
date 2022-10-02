N, Q = map(int, input().split())
L_list = []
sk_list = []
for _ in range(N):
  L = list(map(int, input().split()))
  L_list.append(L)
for _ in range(Q):
  s, k = map(int, input().split())
  print(L_list[s-1][k])
