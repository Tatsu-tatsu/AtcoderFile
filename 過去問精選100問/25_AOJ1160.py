# *
import sys
sys.setrecursionlimit(10**7) # 再帰回数の上限を設定。

dxdy = ((0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,-1),(1,1),(-1,-1))

# マスy,xに隣接する陸を海に置き換え
def dfs(y,x):
    # 現在地を0に置き換え
    field[y][x] = 0
    # 周囲8マスをループ
    for dy, dx in dxdy:
      # 移動後のマスをny,nxとする
      ny = y + dy
      nx = x + dx
      # ny,nxがfield内で陸かどうかを判別
      if 0 <= nx < W and 0 <= ny < H and field[ny][nx] == 1:
          dfs(ny,nx)
    return

while True:
    W, H = map(int, input().split())
    if (W==0 and H==0):
        break
    field = []
    for _ in range(H):
        line = list(map(int, input().split()))
        field.append(line)
    # 島の数
    ans = 0
    for i in range(H):
        for j in range(W):
            if field[i][j] == 1:
                dfs(i,j)
                ans += 1
    print(ans)

# 深さ優先探索（良問）
# 0と1で1のときは接地している8箇所を確認して1の部分をさらに8箇所探索。それを繰り返し、接地している部分をすべて洗い出す。