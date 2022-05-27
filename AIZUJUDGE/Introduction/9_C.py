n = int(input())

ta = 0
ha = 0

for i in range(n):
  a, b = input().split()
  if a == b:
    ta += 1
    ha += 1
  elif a > b:
    ta += 3
  elif a < b:
    ha += 3

print(ta, end=' ')
print(ha)

