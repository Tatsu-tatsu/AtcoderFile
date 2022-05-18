# 以下不可
S = input()

s = list(S)
s.extend(('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''))

count = 0

for i in range(len(S)):
  for j in range(len(S)):
    if s[i+j] == 'A' or s[i+j] == 'C' or s[i+j] == 'G' or s[i+j] == 'T':
      if count < j+1 :
        count = j+1

print(count)

# 以下模範解答
## 思考法：ifで当てはまる時cntを足していき、当てはまらない時、初期化。
S = input()

cnt = 0
ans = 0
a = ['A', 'C', 'G', 'T']

for i in S:
  if i in a:
    cnt += 1
    ans = max(ans, cnt)
  else:
    cnt = 0

print(ans)