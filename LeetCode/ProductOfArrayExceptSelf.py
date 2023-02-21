class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    result = 1
    no_zero = 1
    zero_count = 0
    for num in nums:
      if num == 0:
        result *= 0
        zero_count += 1
      else:
        result *= num
        no_zero *= num
    ans = []
    for num in nums:
      if num == 0:
        if zero_count >= 2:
          ans.append(0)
        else:
          ans.append(no_zero)
        continue
      ans.append(int(result // num))
    return ans
