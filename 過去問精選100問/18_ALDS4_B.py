import bisect
N = int(input())
S = list(map(int, input().split())) + [1000000000000]
q = int(input())
T = list(map(int, input().split()))
ans = 0
for t in T:
  index = bisect.bisect_left(S, t)
  if S[index] == t:
    ans += 1
print(ans)

# bisectは二部探索に使用
# bisectは探索をするbisectと探索と挿入もするinsortの2つが大きくある。
# 大きな数字を検索したとき、一番右端に入れようとするのでindex番号が既存のものを超えるので一つ配列に大きな数字を足して調整する。