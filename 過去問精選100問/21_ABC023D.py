# この問題は、「すべての風船を高度 x 以内で割ることは可能か判定せよ。」という問題へと読み替える。
# これは凄い。関数の置き方が勉強になる。
def is_ok(x): # 特にこの関数凄い。
    ls = []
    for i in range(N):
        ls.append((x-H[i])//S[i]) # いつまでに割れば良いか
    ls.sort() # 期限が近いものから先にわる
    for n in range(N):
        if (ls[n] < n): 
            return False # 時間ぎれ
    return True

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

N = int(input())
H = []
S = []
INF = 10**14 # これは取れる得点の最大値以上であれば良い。
for _ in range(N):
  h, s = map(int, input().split())
  H.append(h)
  S.append(s)
print (meguru_bisect(0,INF))

