N = int(input())
a = []
b = []
for _ in range(N):
  A, B = map(int, input().split())
  a.append(A)
  b.append(B)
a.sort()
b.sort()
am = a[N//2]
bm = b[N//2]
ans = 0
for i in range(N):
  ans += abs(a[i] - am) + abs(b[i] - bm) + abs(b[i] - a[i])
print(ans)

# Point：A<Bであること。ここから独立の問題として解くことが出来る。
# 別々にAとBを分けてそれぞれの中央値から入り口と出口を出す。
