# 以下模範解答
# 入力が複数行の場合があるので下で対応
import sys
texts = sys.stdin.read()
texts = texts.lower()

cnt = [0]*26

letters = 'abcdefghijklmnopqrstuvwxyz'

for x in texts:
  for i in range(26):
    if x == letters[i]:
      cnt[i] += 1

for i in range(26):
  print(letters[i]+":"+str(cnt[i]))
