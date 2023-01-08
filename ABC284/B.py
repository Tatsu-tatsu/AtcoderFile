# メモ
# 計算回数が問題になりそうだから別解を作ったが、最初のままで良かった。
# 問題文の読みミス
T = int(input())
for i in range(T):
  # ans = 0
  N = int(input())
  test = list(map(int,input().split()))
  test = list(map( lambda x:x%2,test))
  print(test.count(1))
  # for j in range(N):
  #   if test[j] % 2 == 1:
  #     ans += 1
  # print(ans)