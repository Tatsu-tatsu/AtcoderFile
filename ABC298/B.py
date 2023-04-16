N = int(input())
A = []
B = []
for _ in range(N):
  a = list(map(int, input().split()))
  A.append(a)
for _ in range(N):
  b = list(map(int, input().split()))
  B.append(b)
for _ in range(4):
  flag = True
  for i in range(N):
    if flag == False:
      break
    for j in range(N):
      if A[i][j] == 1:
        if B[i][j] != 1:
          flag = False
  if flag == True:
    print("Yes")
    exit()
  now = A
  A = [[] for _ in range(N)]
  for s in range(N):
    for t in range(N):
      A[s].append(now[N-1-t][s])
print("No")
