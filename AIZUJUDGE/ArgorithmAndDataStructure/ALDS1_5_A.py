# 全探索
# 以下は動的計画法で解いた。bit全探索による解法も良い。
n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

max = sum(A)
nums = [False for _ in range(max+1)]
for a in A:
  for i in reversed(range(max+1)):
    if nums[i]:
      if i+a <= max+1:
        nums[i+a] = True
  nums[a] = True
for m in M:
  if m > max:
    print("no")
  else:
    if nums[m]:
      print("yes")
    else:
      print("no")

# 再帰関数による解法（計算量：2^n）実際には、O(q*2^n)
# 以下WAになるが、基本の解法は合ってる。
n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

def solve(i, t): #i:index, t:ターゲット
  if A[i] == t:
    return True
  elif A[i] > t:
    return False
  else:
    if i == n-1:
      return False
    res = solve(i+1, t) or solve(i+1, t-A[i])
    return res

for m in M:
  if solve(0, m):
    print("yes")
  else:
    print("no")