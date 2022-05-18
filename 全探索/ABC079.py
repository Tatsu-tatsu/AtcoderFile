# bit全探索の基礎中の基礎
## bit全探索はやり方が全部同じなので慣れたら楽らしい。
## コツ：for文で考えられる全パターンを回す。→中にfor文でbit演算で特定の個数回す（今回は3箇所なので3）→if文で分ける。
S = input()

for i in range(2**3):
  ttl = int(S[0])
  ans = S[0]
  for j in range(3):
    if (i>>j) & 1 :
      ttl += int(S[j+1])
      ans += "+" + S[j+1]
    else: 
      ttl -= int(S[j+1])
      ans += "-" + S[j+1]
  if ttl == 7:
    ans += "=7"
    print(ans)
    exit()
