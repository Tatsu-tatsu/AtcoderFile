N = int(input())
S = input()
places = set()
now = (0, 0)
places.add(now)
for s in S:
  if s == 'L':
    now = (now[0]-1, now[1])
  elif s == 'R':
    now = (now[0]+1, now[1])
  elif s == 'U':
    now = (now[0], now[1]+1)
  elif s == 'D':
    now = (now[0], now[1]-1)
  if now in places:
    print('Yes')
    exit()
  places.add(now)
print('No')