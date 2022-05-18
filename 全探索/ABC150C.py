N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# 以下ライブラリを使った模範解答（順列列挙）
## itertoolsのpermutationsを使う。
## perのリストに入っているものは(A, B)のように入っている。(タプルで出力される。)なのでlistではなく、tupleを用いる。
import itertools
N = int(input())

P=tuple(map(int, input().split()))
Q=tuple(map(int, input().split()))

per = list(itertools.permutations(range(1,N+1)))
p = per.index(P)
q = per.index(Q)
print(abs(p-q))