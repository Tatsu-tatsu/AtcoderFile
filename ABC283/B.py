N = int(input())
A = list(map(int,input().split()))
Q = int(input())
for i in range(Q):
  li = list(map(int,input().split()))
  if li[0] == 1:
    A[li[1]-1] = li[2]
  if li[0] == 2:
    print(A[li[1]-1])
