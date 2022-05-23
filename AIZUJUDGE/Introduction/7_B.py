n = []
x = []

while n == [] or n[-1] > 0 :
  a, b = map(int, input().split())
  n.append(a)
  x.append(b)

count = 0

# 配列の数から最後の0を引いた問題数分ループ。
for s in range(len(n)-1):
  # i は１つ目の足し算用。
  for i in range(1, n[s]+1):
    # j は2つ目の足し算用。
    for j in range(i+1, n[s]+1):
      # k は3つ目の足し算用。
      for k in range(j+1, n[s]+1):
        if i + j + k == x[s]:
          count += 1
  print(count)
  count = 0

# 4重ループになると、何がどこで行われているかわからなくなる。
# 入れ子構造になるときは、すべて言葉でメモしておくのが良さそう。