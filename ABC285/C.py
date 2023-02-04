S = list(input())
ans = 0
for i in range(len(S)):
  ans += int(ord(S[i]) - ord('A') + 1) * int(pow(26, len(S)-i-1))
print(ans)
