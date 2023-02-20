from collections import defaultdict
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    maps = defaultdict(int)
    for num in nums:
      maps[num] += 1
    for key in maps.keys():
      if target - key in maps.keys():
        if key == target - key:
          if maps[key] >= 2:
            return [nums.index(key), nums.index(key, nums.index(key)+1)]
        else:
          return [nums.index(key), nums.index(target-key)]