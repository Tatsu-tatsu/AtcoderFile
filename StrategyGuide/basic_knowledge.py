# ▽様々な所で使えるパーツや知識を集める。
S = input()
s = list(S)
s.extend(('', '')) # s.extend()は戻り値がNone。2行で書く。

# 文字列を2倍にする
s = "ABC"
s = s * 2
print(s) # 'ABCABC'

# 文字列からの検索
if "BCA" in s: # s = "ABCABC"。, 中にあるときは戻り値がtrue
  print("Yes")

# 配列の初期化
l = [0] * 3 # [0, 0, 0]

# 配列の結合
l2 = [1, 2, 3]
# joinで配列の結合。mapですべてをstrにする。
word = "".join(map(str, l2)) ## 123

lst = [24, 16]
# リストの要素を取得
for elem in lst:
  print(elem)
## 24
## 16

# enumerate関数でリストの要素とindexを同時に取得することが出来る。
for i, elem in enumerate(lst):
  print(i, elem)
## 0 24
## 1 16

# 辞書型のfor文の処理
d = {'key1': 1, 'key2': 2}

# 辞書型をそのまま回すとkeyが一覧で取れる。d.keys()も可能。
for k in d:
  print(k)
## key1
## key2

# 辞書型で d.values()を取ると、valueが一覧で取れる。
for v in d.values():
  print(v)
## 1
## 2

# 辞書型で d.items()を取ると、keyとvalueが一覧で取れる。
for k, v in d.items():
  print(k, v)
## key1 1
## key2 2

# f-string:フォーマット済みの文字列リテラルを生成出来る。str()より簡単。
a=1
b=2
print(f"{a}+{b}={a + b}")

# 繰り返し構文 while 条件式: 処理 →whileは条件式がtrueの間繰り返す。
i=0
while i<10:
  print("Hello")
  i +=1

# 出力を横に何個も並べる方法
for i in range(5):
  print('a', end="") ## aaaaaとなる。
print() ## これを最後に入れることでfor文が終了して以降の文章をいつもどおりにする。

from sys import exit
exit() # exitは終了させる。import必要