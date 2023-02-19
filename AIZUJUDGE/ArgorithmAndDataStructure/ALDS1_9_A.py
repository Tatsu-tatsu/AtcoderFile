N = int(input())
A = list(map(int, input().split()))
for i, a in enumerate(A, 1):
  print(f'node {i}: key = {a}, ', end='')
  if i // 2 != 0:
    print(f'parent key = {A[i//2-1]}, ', end='')
  if i * 2 <= N:
    print(f'left key = {A[i*2-1]}, ', end='')
  if i * 2 + 1 <= N:
    print(f'right key = {A[i*2]}, ', end='')
  print()