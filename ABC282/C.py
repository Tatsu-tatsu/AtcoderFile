N = int(input())
S = list(input())
k = 0
for i in range(len(S)):
  if k % 2 == 0:
    if S[i] == ',':
      S[i] = '.'
    elif S[i] == '"':
      k += 1
  elif k % 2 == 1:
    if S[i] == '"':
      k += 1
print("".join(S))
