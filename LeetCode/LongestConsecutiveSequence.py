class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0
    nums_set = set(nums)
    nums_list = list(nums_set)
    nums_list.sort()
    check = nums_list[0]
    ans = 0
    now = 1
    for i in range(1, len(nums_list)):
      if nums_list[i] == check + 1:
        now += 1
        check += 1
      else:
        ans = max(ans, now)
        now = 1
        check = nums_list[i]
    ans = ans = max(ans, now)
    return ans