N = int(input())

list = []
for i in range(9):
  list.append(i+1)

count = 0

for i in range(9):
  for j in range(9):
    ans = list[i] * list[j]
    if ans == N :
      count = 1

if count == 0:
  print("No")
elif count == 1:
  print("Yes")

# 以下模範解答
## exit()は終了させるもの。importしておく必要がある。
from sys import exit

N = int(input())

for i in range(1, 10):
  for j in range(1, 10):
    if N == i * j :
      print("Yes")
      exit()

print("No")
