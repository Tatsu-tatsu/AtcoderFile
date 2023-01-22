from collections import Counter

N, A, B = map(int,input().split())
S = input()

counter = Counter(S)
most = counter.most_common()[0][1]

default = (len(S) - most) * B
max_A = default // A
max_A_B = (default - max_A*A) //B
for i in range(max_A):
  a = S[0]
  b = S[-1]
  middle = S[1:N]
  S = b + middle+a
  if S == S[::-1]:
    ans = min(ans,(i+1)*A)
  for j in range(max_A_B):
    # todo：全パターン置き換えてみる。
    start = S[0:j]
    end = S[j+1, N]
    S = start+ "a" + end