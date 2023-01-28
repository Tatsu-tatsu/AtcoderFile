# マージソート
# pypyにして通したら計算時間通る。
n = int(input())
S = list(map(int, input().split()))
count = [0]
L = [0]*(250000+2)
R = [0]*(250000+2)
sentinel = 20000000000

def merge(S, left, mid, right):
  n1 = mid - left
  n2 = right - mid
  for i in range(n1):
    L[i] = S[left+i]
  for j in range(n2):
    R[j] = S[mid+j]
  L[n1] = R[n2] = sentinel
  p = 0
  q = 0
  for i in range(left, right):
    count[0] += 1
    if L[p] <= R[q]:
      S[i] = L[p]
      p += 1
    elif L[p] > R[q]:
      S[i] = R[q]
      q += 1

def mergeSort(S, left, right):
  if(right - left > 1):
    mid = (left+right)//2
    mergeSort(S, left, mid)
    mergeSort(S, mid, right)
    merge(S, left, mid, right)

mergeSort(S, 0, n)
for i in range(n-1):
  print(S[i], end=" ")
print(S[n-1])
print(count[0])