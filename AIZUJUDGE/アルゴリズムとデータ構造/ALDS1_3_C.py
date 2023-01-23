# 連結リスト
n = int(input())
items = []
for i in range(n):
  item = input().split()
  if len(item) == 2:
    items.append([item[0], int(item[1])])
  else:
    items.append([item[0]])
nums = []
for item in items:
  if item[0] == "insert":
    nums.insert(0, item[1])
  elif item[0] == "delete":
    if item[1] in nums:
      nums.remove(item[1])
  elif item[0] == "deleteFirst":
    nums.pop(0)
  elif item[0] == "deleteLast":
    nums.pop()
for num in nums:
  print(num, end=' ')
