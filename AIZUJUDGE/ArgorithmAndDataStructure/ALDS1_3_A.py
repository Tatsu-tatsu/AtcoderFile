# スタック
li = input().split()
nums = []
for item in li:
  if item == "+" or item == "-" or item == "*":
    a = nums.pop()
    b = nums.pop()
    if item == "+":
      c = a + b
      nums.append(c)
    elif item == "-":
      c = b - a
      nums.append(c)
    elif item == "*":
      c = a * b
      nums.append(c)
  else:
    nums.append(int(item))
print(nums.pop())