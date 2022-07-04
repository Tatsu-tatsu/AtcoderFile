# 行列の計算や扱い方
import numpy as np
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 行列の積
a2 = np.dot(a, a)

# 標準入力が複数行有り、それをすべて文字列として一つで読み取りたい場合
import sys
texts = sys.stdin.read()

# 数字の桁数の処理
N = 2543
n = str(N)
# 配列にする。
n_array = list(map(int, n))
if "3" in n:
  print("3があるよ")

# 二次元配列以上のsort
data = [['きゅうり',1,4],['いちご',2,6],['にんじん',2,1],['とうふ',1,0]]
# 昇順でソートする
sorted_data = sorted(data, key=lambda x:(x[1], x[2]))
print(sorted_data) #data = [['とうふ',1,0],['きゅうり',1,4],['にんじん',2,1],['いちご',2,6]]

# 配列で検索する際、計算量が多くなる問題→set型を利用（特有の書き方はあるが、ほぼ配列と使い方は一緒）
## 検索スピードは配列が多い。辞書型とset型は圧倒的に早い。
#初期化
s = set()
# 要素追加
s.add(123)

#datetime：日付情報をオブジェクト化して比較等出来る。
import datetime
Atime = datetime.datetime(2022, 7, 4, 17, 7, 42)