N, M = map(int, input().split())

items = {}
count = 0
seen = [False for _ in range(N+1)]
seen[0] = True

for i in range(M):
  p, q = map(int, input().split())
  if p in items.keys():
    items[p].append(q)
  else:
    items[p] = [q]
  if q in items.keys():
    items[q].append(p)
  else:
    items[q] = [p]
flag = False
num = 1
while num in items.keys() and count + 1 <N and not flag:
  for i in range(len(items[num])):
    if seen[items[num][i]]:
      if flag:
        break
      flag = True
      continue
    seen[num] = True
    num = items[num][i]
    flag = False
    count += 1
    break
rightMax = num

flag = False
num = 1
while num in items.keys() and count + 1 <N and not flag:
  for i in range(len(items[num])):
    if seen[items[num][i]]:
      if flag:
        break
      flag = True
      continue
    seen[num] = True
    num = items[num][i]
    flag = False
    count += 1
    break
leftMax = num
if N == 2:
  if count+ 1 ==  N:
    print("Yes")
  else:
    print("No")
else:
  if count+ 1 ==  N and not leftMax in items[rightMax]:
    print("Yes")
  else:
    print("No")