# 以下模範解答
## enumerate()は引数にリストなどを入れると、インデックス番号, 要素の順に取得できる。

N, M = map(int, input().split())

lamp_dat = [list(map(int, input().split()))[1:] for l in range(M)]

switches = [[] for _ in range(N)]
for i, sw_list in enumerate(lamp_dat):
  for sw in sw_list[1:]:
    switches[sw-1].append(i)

lit_cond = int(''.join(input()[::-1].split()), 2)

ans = 0

for st in range(1<<N):
  lamp_status = 0
  for i in range(N):
    for lmp in switches[i]:
      lamp_status = lamp_status ^ (1<<lmp)
  if lamp_status ==lit_cond:
    ans += 1

print(ans)

# 以下別解
N, M = map(int, input().split())
lamps = [list(map(lambda x:int(x)-1, input().split()))[1:] for _ in range(M)]
p = list(map(int, input().split()))
ans = 0

# bit全探索(スイッチの入れ方を全探索する)
# range(2**N)はrange(1 << N)でも問題ない。
for i in range(2**N):
    for r in range(M):  # 全てのランプがついてるかチェック
        on_sum = 0  # ランプrにおいて、onのスイッチの数
        for j in range(N):  # スイッチのj番目について
            if i >> j & 1 and j in lamps[r]:
                on_sum += 1  # スイッチjがランプrに繋がってて、onならon_sum+=1
        if on_sum % 2 != p[r]:  # on_off check
            break  # 一つでもoffなら次のbitに
    else:
        ans += 1
print(ans)
