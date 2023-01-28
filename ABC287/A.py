N = int(input())
plus = 0
for i in range(N):
  item = input()
  if item == "For":
    plus += 1
if (N // 2) < plus:
  print("Yes")
else:
  print("No")