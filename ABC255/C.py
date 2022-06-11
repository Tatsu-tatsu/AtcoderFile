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