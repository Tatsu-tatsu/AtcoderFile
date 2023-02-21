from collections import defaultdict
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    maps = defaultdict(int)
    for num in nums:
      maps[num] += 1
    maps2 = sorted(maps.items(), key=lambda x: x[1], reverse=True)
    ans = []
    check = 0
    for key, v in maps2:
      if check == k:
        break
      ans.append(key)
      check += 1
    return ans