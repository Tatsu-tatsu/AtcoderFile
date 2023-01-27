# 二分探索
# Pythonは関数があるが、0から実装した。
# leftとrightで範囲を絞ることが大事
# 中間は商だけを取れば、問題なし。 
# left側に+1を付けることでwhileを終了させれる。
n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
count = 0

for t in T:
  left = 0
  right = n
  while left < right:
    mid = (left + right) // 2
    if S[mid] == t:
      count += 1
      break
    elif t < S[mid]:
      right = mid
    elif S[mid] < t:
      left = mid + 1

print(count)

# binarySearchを関数化
def binarySearch(S, t):
  left = 0
  right = n
  while left < right:
    mid = (left + right) // 2
    if S[mid] == t:
      return 1
    elif t < S[mid]:
      right = mid
    elif S[mid] < t:
      left = mid + 1
  return 0

for t in T:
  count += binarySearch(S, t)
print(count)