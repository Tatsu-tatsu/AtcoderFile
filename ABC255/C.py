from sys import exit
X, A, D, N = map(int, input().split())
if D < 0 and X>A:
  print(X-A)
  exit()
t = 0
for i in range(N):
  if A + D*(i+1)*1000000000000000000 < X:
    t += (i+1)*1000000000000000000
    continue
  if A + D*(i+1)*100000000000000000 < X:
    t += (i+1)*100000000000000000
    continue
  if A + D*(i+1)*10000000000000000 < X:
    t += (i+1)*10000000000000000
    continue
  if A + D*(i+1)*1000000000000000 < X:
    t += (i+1)*1000000000000000
    continue
  if A + D*(i+1)*100000000000000 < X:
    t += (i+1)*100000000000000
    continue
  if A + D*(i+1)*10000000000000 < X:
    t += (i+1)*10000000000000
    continue
  if A + D*(i+1)*1000000000000 < X:
    t += (i+1)*1000000000000
    continue
  if A + D*(i+1)*100000000000 < X:
    t += (i+1)*100000000000
    continue
  if A + D*(i+1)*10000000000 < X:
    t += (i+1)*10000000000
    continue
  if A + D*(i+1)*1000000000 < X:
    t += (i+1)*1000000000
    continue
  if A + D*(i+1)*100000000 < X:
    t += (i+1)*10000000000
    continue
  if A + D*(i+1)*10000000 < X:
    t += (i+1)*10000000
    continue
  if A + D*(i+1)*1000000 < X:
    t += (i+1)*1000000
    continue
  if A + D*(i+1)*100000 < X:
    t += (i+1)*100000
    continue
  if A + D*(i+1)*10000 < X:
    t += (i+1)*10000
    continue
  if A + D*(i+1)*1000 < X:
    t += (i+1)*1000
    continue
  if A + D*(i+t) == X:
    print(0)
    exit()
  if A + D*(i+t) > X and A+D*(i+t-1) < X:
    p = A+D*(i+t-1)
    q = A + D*i
    if X -p < q - X:
      print(X-p)
    elif X -p > q - X:
      print(q-X)

# 以下模範解答
# 二分探索を使う。
# 等差数列の反転。マイナスはやりにくいので、D>=0になるように正規化する。
# 公差に-1をかける。項数は一緒。元々の最後の項を初項とする。

X, A, D, N = map(int, input().split())
def S(i):
  return A+(i-1)*D

if D<0:
  A = S(N)
  D = D*-1

def search(X):
  # (1)区間[左,右]を指定する。
  l=0
  r=N
  # (4)1<(左-右)となっている間繰り返す。
  while 1 < r-l:
    # (2)中央値が条件を満たすか。
    # (3)右or左を更新する。
    c=(l+r)//2
    if S(c) <= X:
      l=c
    else:
      r=c
  return l,r

if D==0:
  print(abs(A-X))
elif 0< D:
  if X<A:
    print(A-X)
  elif S(N)<=X:
    print(X-S(N))
  else:
    l,r = search(X)
    print(min(X-S(l), S(r)-X))