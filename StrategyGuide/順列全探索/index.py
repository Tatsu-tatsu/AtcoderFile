## itertoolsのpermutationsを使う。
## perのリストに入っているものは(A, B)のように入っている。(タプルで出力される。)なのでlistではなく、tupleを用いる。

# 問題
# 大きさ N の順列 ((1, 2, ..., N) を並び替えてできる数列) P, Q があります。
#大きさ N の順列は N! 通り考えられます。このうち、P が辞書順で a 番目に小さく、Q が辞書順で b 番目に小さいとして、∣a−b∣ を求めてください。
#参考：https://atcoder.jp/contests/abc150/tasks/abc150_c

import itertools
N = int(input())

P=tuple(map(int, input().split()))
Q=tuple(map(int, input().split()))

per = list(itertools.permutations(range(1,N+1)))
p = per.index(P)
q = per.index(Q)
print(abs(p-q))