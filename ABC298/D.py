Q = int(input())
S = "1"
S_nums = []
S_strings = ""
for q in range(Q):
  t = list(map(int, input().split()))
  if len(S) >= 10:
    tmp = int(S) % 998244353
    S_nums.append(tmp)
    if S_strings == "":
      S_strings += str(S)
    S = ""
  if t[0] == 1:
    x = t[1]
    S += str(x)
  elif t[0] == 2:
    if S_strings != "":
      S_now = S_strings[1:]
      S_nums[0] = int(S_now) % 998244353
    else:
      S = S[1:]
  elif t[0] == 3:
    test = ""
    for s in S_nums:
      test += str(s)
    test += S
    ans = int(test) % 998244353
    print(ans)