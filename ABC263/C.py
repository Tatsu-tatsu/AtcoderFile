import itertools
N, M = map(int, input().split())

num = list(range(1, M+1))

patterns = list(itertools.combinations(num, N))

for pattern in patterns:
  for i in range(len(pattern)):
    print(str(pattern[i])+" ", end="")
  print("")

# 所感：pythonのcombinations強すぎ。これだけで終わる。