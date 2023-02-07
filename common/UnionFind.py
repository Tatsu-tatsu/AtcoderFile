class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1] * n

    # xの親を取得
    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    #xを含む集合とyを含む集合を合併
    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # xとyが同じ集合に属しているかの判定（findで=してるだけ）
    def same(self,x,y):
        return self.find(x) == self.find(y)

    # 不明（親を取得はFindでいけるので使ったことがない）
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]