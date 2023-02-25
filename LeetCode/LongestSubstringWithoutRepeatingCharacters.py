from collections import deque
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    items = set()
    que = deque()
    ans = 0
    for item in s:
      if item not in items:
        items.add(item)
        que.append(item)
      else:
        ans = max(ans, len(items))
        while que[0] != item:
          items.remove(que.popleft())
        if len(items) == 0:
          items.add(item)
        que.popleft()
        que.append(item)
    ans = max(ans, len(items))
    return ans
