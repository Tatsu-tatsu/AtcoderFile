N = int(input())
S = input()

count = 0

s = list(S)
s.extend(('', ''))

print(s)
for i in range(N):
  if s[i] == 'A' :
    if s[i+1] == 'B':
      if s[i+2] == 'C':
        count += 1

print(count)

# 学び
## s.extendは戻り値としてNoneを返す。したがって、一行に書かずに2行にする。

# 以下模範解答
N = int(input())
S = input()

result = 0

for i in range(N):
  if S[i:i+2] == 'ABC':
    result += 1

print(result)
