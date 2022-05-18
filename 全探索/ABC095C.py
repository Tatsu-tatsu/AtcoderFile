A, B, C, X, Y = map(int, input().split())

mny = 0

if X > Y:
  cnt = Y
  mny += A * (X - Y)
elif X < Y:
  cnt = X
  mny += B * (Y - X)

if A + B >= 2 * C:
  mny += cnt * 2 * C
elif A + B < 2 * C:
  mny += cnt * (A + B)

print(mny)

# 以下模範解答1
## A+B <= 2*Cのときは簡単。それ以外のとき、考えられるパターンを両方計算してmin()で小さい方を取る。
A, B, C, X, Y = map(int, input().split())

if A+B <= 2*C:
  print(A*X+B*Y)
else:
  if X <= Y:
    print(min(2*C*Y, 2*C*X+B*(Y-X)))
  else:
    print(min(2*C*X, 2*C*Y+A*(X-Y)))

# 以下模範解答2
## Cピザの個数をZとする。そうすると、式はA(X-Z)+B(Y-Z)+2CZ円になる。
## max()を使うことでマイナスの部分になると自動で0に出来る。
A, B, C, X, Y = map(int, input().split())
ans = 2*(5000*10**5)
for Z in range(10**5+1):
  total = A*max(X-Z, 0)+B*max(Y-Z, 0)+2*C*Z
  ans = min(total,ans)
print(ans)