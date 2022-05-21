N = int(input())

ans = 10000000000000

for i in range(1, 100000 + 1):
  if N % i == 0:
    a = int(N / i)
    d = max(len(str(a)), len(str(i)))
    if ans > d:
      ans = d

print(ans)

# 学び：計算量を10^6以下にする。今回は10^12だったので半分以下にする必要性がある。
# 積において半分にで良い→桁数が半分で良い。2で割るのでは無い。