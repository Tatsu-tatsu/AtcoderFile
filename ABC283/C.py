S = list(input())
ans = 0
a = 0
count = 0
for item in S:
  if item == '0':
    count += 1
    if count == 2:
      a += 1
      count = 0
  else:
    count = 0
print(len(S) - a)