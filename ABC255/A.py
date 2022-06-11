R, C = map(int, input().split())
A = []
for i in range(2):
  s, t = map(int, input().split())
  A.append(s)
  A.append(t)
if R ==1:
  print(A[C-1])
else:
  print(A[C+1])