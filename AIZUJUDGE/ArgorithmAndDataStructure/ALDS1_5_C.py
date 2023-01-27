# コッホ曲線
# 再帰関数の練習。以下はどこか間違っているが方向性は問題なし。
import math
n = int(input())

p = [0.00000000, 0.00000000]
q = [100.00000000, 0.00000000]

def koch(d, p, q):
  if d == 0:
    return
  s = []
  t = []
  u = []
  s.append((p[0]*2+q[0]*1) / 3)
  s.append((p[1]*2+q[1]*1) / 3)
  t.append((p[0]*1+q[0]*2) / 3)
  t.append((p[1]*1+q[1]*2) / 3)
  u.append((t[0] - s[0]) *math.cos(math.radians(60)) - (t[1] - s[1])*math.sin(math.radians(60)) + s[0])
  u.append((t[0] - s[0])*math.sin(math.radians(60)) + (t[1] -s[1])*math.cos(math.radians(60)) + s[1])

  koch(d-1, p, s)
  print('{:.8g}'.format(s[0]), end=" ")
  print('{:.8g}'.format(s[1]))
  koch(d-1, s, u)
  print('{:.8g}'.format(u[0]), end=" ")
  print('{:.8g}'.format(u[1]))
  koch(d-1, u, t)
  print('{:.8g}'.format(t[0]), end=" ")
  print('{:.8g}'.format(t[1]))

print(p[0], end=" ")
print(p[1])
koch(n, p, q)
print(q[0], end=" ")
print(q[1])