N = int(input())
A = list(map(int, input().split()))

place = [0]*4
P = 0

for i in range(N):
  place[0] = 1
  if place[3] >= 1:
    P += place[3]
    place[3] = 0
  if place[2] >= 1:
    if A[i] >=2:
      P += place[2]
    else:
      place[3] = place[2]
    place[2] = 0
  if place[1] >= 1:
    if A[i] >= 3:
      P += place[1]
    else:
      s = 1+A[i]
      place[s] = place[1]
    place[1] = 0
  if place[0] >= 0:
    if A[i] >=4:
      P += place[0]
    else:
      s = A[i]
      place[s] = place[0]
    place[0] = 0

print(P)




