s = list(input())
for i in range(len(s)):
  if i % 2 == 0:
    s[i], s[i+1] = s[i+1], s[i]
print(('').join(s))