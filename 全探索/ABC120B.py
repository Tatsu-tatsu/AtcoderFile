A, B, K= map(int, input().split())

s = []

for i in range(1, 101):
  if A % i == 0 and B % i == 0:
    s.append(i)

print(s[K-1])

#回答問題なし