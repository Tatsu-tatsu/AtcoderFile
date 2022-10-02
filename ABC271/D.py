N, S = map(int, input().split())
ab = []
for _ in range(N):
  a, b = map(int, input().split())
  ab.append((a, b))
ans = ""
def dfs(card, aORb):
  if aORb == 0:
    ans += "H"
  elif aORb == 1:
    ans += "T"
  num = S - ab[card][aORb]
  if num == 0:
    print("Yes")
    print(ans)
    exit()
  if num > 0:
    for i in range(card+1, N):
      for j in range(2):
        dfs(i, j)
        ans = ans[:-1]

for i in range(N):
  for j in range(2):
    dfs(i, j)
    ans = ans[:-1]

print("No")

# 以下模範解答
# 動的計画法で解く。
n,s = map(int,input().split())
card_list = []
for _ in range(n):
    a,b = map(int,input().split())
    card_list.append([a,b])
    
#dpの作成
dp = [["No" for _ in range(s)] for _ in range(n)]
 
for i in range(len(card_list[0])):
    if (i == 0)and(card_list[0][i]-1 < s) :
        dp[0][card_list[0][i]-1] = "H"
    elif (i == 1)and(card_list[0][i]-1 < s):
        dp[0][card_list[0][i]-1] = "T"
    
for i in range(1,n):
    for j in range(s):
        card = card_list[i]
        if (dp[i-1][j-card[0]] != "No")and(j-card[0] >= 0):
            dp[i][j] = dp[i-1][j-card[0]]
            dp[i][j] += "H"
        elif (dp[i-1][j-card[1]] != "No")and(j-card[1] >= 0):
            dp[i][j] = dp[i-1][j-card[1]]
            dp[i][j] += "T"
            
judge = dp[n-1][s-1]
if judge != "No":
    print("Yes")
    
print(judge)