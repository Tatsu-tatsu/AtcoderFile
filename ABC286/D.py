N, X = map(int,input().split())
count = X
AB = []
for i in range(N):
  ab = list(map(int,input().split()))
  AB.append(ab)
AB.sort(reverse=True)
memo_n = []
j = 0
times = 0
# 1回目
for i in range(j,N):
  max_n = count // AB[i][0]
  if max_n >=1:
    memo_n.append([i, count, times])
  if AB[i][1] <= max_n:
    count -= AB[i][0]*AB[i][1]
  elif AB[i][1] > max_n:
    count -= AB[i][0]*max_n
  if count == 0:
    print("Yes")
    exit()
# 2回目以降
while len(memo_n)>=1 :
  j = memo_n[0][0]
  count = memo_n[0][1]
  times += memo_n[0][2] + 1
  memo_n = []

  max_n = count // AB[j][0] - times
  if max_n >=1:
    memo_n.append([j, count, times])
  if AB[j][1] <= max_n:
    count -= AB[i][0]*AB[j][1]
  elif AB[j][1] > max_n:
    count -= AB[j][0]*max_n
  if count == 0:
    print("Yes")
    exit()

  for i in range(j+1,N):
    max_n = count // AB[i][0]
    if max_n >=1:
      times = 0
      memo_n.append([i, count, times])
    if AB[i][1] <= max_n:
      count -= AB[i][0]*AB[i][1]
    elif AB[i][1] > max_n:
      count -= AB[i][0]*max_n
    if count == 0:
      print("Yes")
      exit()
print("No")

