# データ構造の応用
items = input().split()
nums = []
s_ans = []
for i in range(len(items)):
  if items[i] == "\\":
    nums.append(i)
  elif items[i] == "/" and nums:
    num = nums.pop()
    s_memo = i - num
    if nums:
      s = s_ans.pop()
      s_ans.append(s+s_memo)

