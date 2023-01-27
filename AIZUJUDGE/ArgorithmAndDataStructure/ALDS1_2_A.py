# バブルソート
N = int(input())
A = list(map(int, input().split()))
count = 0

def bubbleSort(A, N):
  count = 0
  flag = True
  while flag:
    flag = False
    for j in reversed(range(1, N)):
      if A[j] < A[j-1]:
        A[j], A[j-1] = A[j-1], A[j]
        count += 1
        flag = True
  return A, count

new_A, count = bubbleSort(A, N)
for a in new_A:
  print(a, end=' ')
print()
print(count)