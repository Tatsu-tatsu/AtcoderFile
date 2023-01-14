# メモ：文字列を配列に毎回せず文字列のまま見る方法が最短
S = list(input())
T = list(input())
count = 0
i = 0
for s in S:
  if T[i] == s:
    i += 1
    count += 1
  else:
    i = 0
  if count == len(T):
    print("Yes")
    exit()
print("No")

# 模範解答
s = input()
t = input()

ans = "No"
if 0 < s.count(t):
    ans = "Yes"

print(ans)

# 模範解答2
S = input()
T = input()

if T in S:
    print('Yes')
else :
    print('No')