# 回答
nums = []
n = int(input())
for i in range(n):
  nums.append(int(input()))
memo_minN = nums[0]
maxN = 0
for i in range(1, len(nums)):
  num = nums[i]
  if maxN <= num:
    maxN = num
    minN = memo_minN
    print(maxN)
  memo_minN = min(memo_minN, num)
print(maxN - minN)

# メモ：値の大小を測っても意味がない。答えの大小を測るべき。答えに対して真っ直ぐ解く。
# maxの値が変わったときに値を変更していく。

# 回答2
nums = []
n = int(input())
for i in range(n):
  nums.append(int(input()))
minN = nums[0]
maxN = 0
maxV = 0
for i in range(1, len(nums)):
  num = nums[i]
  maxV = max(maxV, num - minN)
  minN = min(minN, num)
print(maxV)

# 模範解答
nums = []
n = int(input())
for i in range(n):
  nums.append(int(input()))
minV = nums[0]
maxV = -20000000000000000 # ここをこう設定しないとエラーになる。
for i in range(1, n):
  maxV = max(maxV, nums[i]-minV)
  minV = min(minV, nums[i])
print(maxV)