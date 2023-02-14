S = list(input())
for i in range(len(S)):
  if S[i] == "0":
    S[i] = "1"
  elif S[i] == "1":
    S[i] = "0"
print(''.join(S))
