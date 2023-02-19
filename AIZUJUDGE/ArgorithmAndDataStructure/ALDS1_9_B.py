def maxHeapify(i):
  l = 2 * i
  r = 2 * i + 1
  largest = i
  if r <= H and A[r] > A[largest]:
    largest = r
  if l <= H and A[l] > A[largest]:
    largest = l
  if largest != i:
    A[i], A[largest] = A[largest], A[i]
    # 以下：変更があった場合、それ以下の部分の変更の可能性があるので、再帰的に呼び出す
    maxHeapify(largest)

H = int(input())
A = [None] + list(map(int, input().split()))
for i in range(H//2, 0, -1):
  maxHeapify(i)
for i in range(1, H+1):
  print(A[i], end=' ')