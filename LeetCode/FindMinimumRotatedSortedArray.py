# 二分探索練習
class Solution:
  def findMin(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    if nums[0] < nums[-1]:
      return nums[0]
    left, right = 0, len(nums) - 1
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] > nums[mid + 1]:
        return nums[mid + 1]
      if nums[mid - 1] > nums[mid]:
        return nums[mid]
      if nums[mid] > nums[0]:
        left = mid + 1
      else:
        right = mid - 1
    return nums[left]

# 別解（こちらの方が良い）
class Solution:
  def findMin(self, nums: List[int]) -> int:
    left,right = 0,len(nums)-1
    while left < right:
      mid = (right+left)//2
      if nums[mid] > nums[right]:
        left = mid + 1 # mid + 1することでwhile文の条件を満たす
      else:
        right = mid
    return nums[left]