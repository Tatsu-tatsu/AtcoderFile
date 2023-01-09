# TLE
# 適切なデータ構造の扱いを理解して行うとO(|S|)となり、問題無くなる。
# 今見ている所をまとめて管理するという考え。まとまりを作る。
S = list(input())
count = 0
box = set()
for i in range(len(S)):
  if S[i] == '(':
    continue
  elif S[i] == ')':
    for j in range(i):
      if S[i-j-1] == '(':
        if count == 0:
          break
        else:
          count -= 1
      elif S[i-j-1] == ')':
        count += 1
      else:
        if S[i-j-1] in box:
          box.remove(S[i-j-1])
  else:
    if S[i] in box:
      print('No')
      exit()
    else:
      box.add(S[i])
print('Yes')

# 解答2（考察を見た後）
S = list(input())
# 一時中断用に塊で保存する
time = []
# 辞書型で箱に入っているかどうかを確認
box = {}
# 現状を保存
now = set()
for s in S:
  if s == '(':
    time.append(now)
    now = set()
    continue
  if s== ')':
    for i in now:
      box[i] = False
    now = time.pop()
    continue
  now.add(s)
  if s not in box.keys():
    box[s] = True
  else:
    if box[s]:
      print('No')
      exit()
print('Yes')