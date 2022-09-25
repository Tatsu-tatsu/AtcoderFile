import itertools
N = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
lists = []
for i in range(N):
  lists.append(i+1)
pattern_list = list(itertools.permutations(lists, N))
p_num = pattern_list.index(p)
q_num = pattern_list.index(q)
ans = abs(p_num - q_num)
print(ans)

# 特になし。
# itertools.permutations(lists, N)これで順番に全パターン作成出来る。
# tuple型やindexの使い方を学べる。