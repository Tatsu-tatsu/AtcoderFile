# 各桁数を足していく。
# 考え方:文字列にして一つずつを取る。
# 文字列の扱い方と数字の扱い方がわかる良問
x = []
while x == [] or x[-1] != 0:
  a = int(input())
  x.append(a)

count = 0

for num in x:
  if num == 0:
    break
  item = str(num)
  for i in item:
    count += int(i)
  print(count)
  count = 0