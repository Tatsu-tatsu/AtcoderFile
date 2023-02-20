from collections import defaultdict
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    maps = defaultdict(list)
    for item in strs:
      key = "".join(sorted(item))
      maps[key].append(item)
    ans = []
    for item in maps.values():
      ans.append(item)
    return ans