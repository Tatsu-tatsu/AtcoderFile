def increase_key(i, key):
  if key < A[i]:
    return
  A[i] = key
  while i > 1 and A[i//2] < A[i]:
    A[i], A[i//2] = A[i//2], A[i]
    i //= 2

def insert(key):
  global H
  H += 1
  A.append(-1)
  increase_key(H, key)

def maxHeapify(i):
  global H
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

def extract():
  global H
  maxv = A[1]
  A[1] = A[H]
  A.pop(-1)
  H -= 1
  maxHeapify(1)
  return maxv


H = 0
A = [None]
message = input().split()
while message[0] != "end":
    if message[0] == "insert":
        insert(int(message[1]))
    elif message[0] == "extract":
        print(extract())
    message = input().split()