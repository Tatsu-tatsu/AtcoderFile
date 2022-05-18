from sys import exit
N = int(input())

cnt = 0
ans = 0

if N < 105:
  print(0)
  exit()
else:
  for j in range(105, N+1):
    cnt = 0
    for i in range(1, N+1, 2):
      if j % i == 0:
        cnt += 1 
    if cnt == 8:
      ans += 1

print(ans)

#回答問題なし