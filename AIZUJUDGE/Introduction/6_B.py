start = {"S":[], "H":[], "C":[], "D":[]}
for i in range(1, 14):
  start["S"].append(i)
  start["H"].append(i)
  start["C"].append(i)
  start["D"].append(i)
## list型に追加していきたいときは、append()を使う。

li = []

n = int(input())
for i in range(n):
  a, b =input().split()
  start[a].remove(int(b))

print(start)

## 辞書型をin の後ろに入れてfor文を回すと、keyの値が取れる。
for key in start:
## リスト型をin の後ろに入れてfor文を回すと、配列の中身が取れる。
  for item in start[key]:
    print(key, item)

# 良問。辞書型とリスト型を正しく理解して正しく扱えないと駄目。
# URL:https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_B&lang=ja