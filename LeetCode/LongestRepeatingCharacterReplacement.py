# 以下、一部解けず。
# ポイント：kをどのように比較するかが重要
class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    ans = 0
    data = []
    check = False
    if k == 0:
      count = 0
      name = ""
      for st in s:
        if name == st:
          count += 1
        else:
          ans = max(ans, count)
          count = 1
          name = st
      ans = max(ans, count)
      return ans
    for i in range(len(s)):
      if len(data) == 0:
        data.append([s[i], 1, 0])
      else:
        for d in data:
          if d[0] == s[i]:
            d[1] += 1
            if d[2] == k:
              check = True
          else:
            if d[2] < k:
              d[2] += 1
              d[1] += 1
            else:
              ans = max(ans, d[1])
              data.remove(d)
      if check:
        data.append([s[i], 1, 0])
        check = False
    for d in data:
      ans = max(ans, d[1])
    return ans

# 解法
# 重要：2点を決め、範囲内にある文字のカウントを取り、それが満たすかどうかを毎回チェックする
# →文字をベースに考えてはいけない。範囲の中にあるかどうかだけをチェックする。満たさなければ左端をずらす。
class Solution(object):
  def characterReplacement(self, s, k):
    maxlen, largestCount = 0, 0
    arr = defaultdict(int)
    for idx in range(len(s)):
      arr[s[idx]] += 1
      largestCount = max(largestCount, arr[s[idx]])
      if maxlen - largestCount >= k:
        arr[s[idx - maxlen]] -= 1
      else:
        maxlen += 1
    return maxlen
# 解答確認後
from collections import defaultdict
class Solution(object):
  def characterReplacement(self, s, k):
    count = defaultdict(int)
    ans = 0
    windowLength = 0
    for i in range(len(s)):
      count[s[i]] += 1
      windowLength += 1
      if windowLength - max(count.values()) <= k:
        ans = max(ans, windowLength)
      else:
        count[s[i-windowLength+1]] -= 1
        windowLength -= 1
    ans = max(ans, windowLength)
    return ans