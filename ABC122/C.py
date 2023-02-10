# 累積和：練習問題
N, Q = map(int, input().split())
S = input()
lr = []
for i in range(Q):
  l, r = map(int, input().split())
  lr.append([l, r])
counts = [0] * N
for i in range(1, N):
  if S[i-1] == "A" and S[i] == "C":
    counts[i] = counts[i-1]+1
  else:
    counts[i] = counts[i-1]
for i in range(Q):
  l = lr[i][1]
  r = lr[i][0]
  print(counts[l-1] - counts[r-1])
