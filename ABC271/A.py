N = int(input())
a = hex(N)
b = a[2:]
if len(b) == 2:
  print(b.upper())
elif len(b) == 1:
  print("0" + b.upper())
