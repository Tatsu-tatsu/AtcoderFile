import collections
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    ans = []
    set_nums = set(nums)
    c = collections.Counter(nums)
    for num1 in set_nums:
      for num2 in set_nums:
        if num1 == num2 and c[num1] < 2:
          continue
        if -num1-num2 in set_nums:
          if -num1-num2 == num1 and c[num1] < 2:
            continue
          if -num1-num2 == num2 and c[num2] < 2:
            continue
          if -num1-num2 == num1 and -num1-num2 == num2 and c[num1] < 3:
            continue
          ans.append([num1, num2, -num1-num2])
    ans = list(set([tuple(sorted(t)) for t in ans]))
    return ans
