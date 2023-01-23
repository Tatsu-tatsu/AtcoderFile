# キュー
n, q = map(int, input().split())
now = 0
items = []
for i in range(n):
  tmps = input().split()
  item = [tmps[0], int(tmps[1])]
  items.append(item)

while items:
  item = items.pop(0)
  if item[1] <= q:
    now += item[1]
    print(item[0]+ " " +str(now))
  elif item[1] > q:
    remaining = item[1] - q
    now += q
    items.append([item[0], remaining])

