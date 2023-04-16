N = int(input())
S = list(input())
flag = False
for s in S:
  if s == "o":
    flag = True
  elif s == "x":
    print("No")
    exit()
if flag:
  print("Yes")
else:
  print("No")