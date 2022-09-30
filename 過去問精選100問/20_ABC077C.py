import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
B.append(10000000000)
C.append(10000000000)
A.sort()
B.sort()
C.sort()
ans = 0
for a in A:
  indexB = bisect.bisect_left(B, a)
  if B[indexB] == a:
    indexB = bisect.bisect_left(B, a+1)
  for b in B[indexB:]:
    indexC = bisect.bisect_left(C, b)
    if C[indexC] == b:
      indexC = bisect.bisect_left(C, b+1)
    ans += len(C) - 2 - indexC
print(ans)
# 上論理ズレ
# for重複等はややこしくなるので基本は避ける。それ以外の方法はないか考える。
# 模範解答
# Point：3段なので中段を固定して考える。
# bisect_left,bisect_rightを使いこなす。
import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
for b in B:
  a = bisect.bisect_left(A, b)
  c = bisect.bisect_right(C, b)
  ans += a * (len(C)-c)
print(ans)