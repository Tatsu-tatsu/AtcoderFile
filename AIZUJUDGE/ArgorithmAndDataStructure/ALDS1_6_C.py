# クイックソート
# 一部問題あるが、優先順位低いのでパス
n = int(input())
cards = []
cards2 = []
for i in range(n):
  item = input().split()
  cards.append(item)
  cards2.append(item)
L = [0]*(250000+2)
R = [0]*(250000+2)
sentinel = 20000000000

def merge(S, count, left, mid, right):
  n1 = mid - left
  n2 = right - mid
  for i in range(n1):
    L[i] = int(S[left+i][1])
  for j in range(n2):
    R[j] = int(S[mid+j][1])
  L[n1] = R[n2] = sentinel
  p = 0
  q = 0
  for i in range(left, right):
    count = count + 1
    if L[p] <= R[q]:
      S[i][1] = L[p]
      p += 1
    elif L[p] > R[q]:
      S[i][1] = R[q]
      q += 1

def mergeSort(S, count, left, right):
  if(right - left > 1):
    mid = (left+right)//2
    mergeSort(S, count, left, mid)
    mergeSort(S, count, mid, right)
    merge(S, count, left, mid, right)

def partition(A, p, r):
  x = int(A[r][1])
  i = p-1
  for j in range(p, r):
    if int(A[j][1]) <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r], A[i+1]
  return i+1

def quickSort(cards, n, p, r):
  if p < r:
    q = partition(cards, p, r)
    quickSort(cards, n, p, q-1)
    quickSort(cards, n, q+1, r)

stable = True
mergeSort(cards, n, 0, n)
quickSort(cards2, n, 0, n-1)

for i in range(n):
  if cards[i][0] != cards2[i][0]:
    stable = False

if stable:
  print("Stable")
else:
  print("Not stable")

for i in range(n):
  print(cards2[i][0], end=" ")
  print(cards2[i][1])

