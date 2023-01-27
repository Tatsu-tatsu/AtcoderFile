# ハッシュ法
# Pythonでは、ハッシュ（ハッシュテーブル）のことを辞書と呼ぶ。
# 以下の解法はハッシュ法ではない。辞書の使い方も違う。必要性をそこまで感じなかったのでスキップ。
# C言語では桁数のメモリ問題等で数値に変換し、保存せざるを得なかった。
# 数値にするといつか衝突が起きる。
n = int(input())
dictionary = set()
for i in range(n):
  item = input().split()
  if item[0] == "insert":
    dictionary.add(item[1])
  elif item[0] == "find":
    if item[1] in dictionary:
      print("yes")
    else:
      print("no")