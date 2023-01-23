# 選択ソート
N = int(input())
A = list(map(int, input().split()))

def selectionSort(A, N):
  count = 0
  for i in range(N):
    minj = i
    for j in range(i, N-1):
      if A[j] < A[minj]:
        minj = j
    A[j], A[minj] = A[minj], A[j]
    count += 1
  return A, count

new_A, count = selectionSort(A, N)
print(new_A)
print(count)