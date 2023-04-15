# 二分探索：回転した配列の中から値を探す。回転の分岐点があるかないかで場合分け。
class Solution:
  def search(self, nums: List[int], target: int) -> int:
    if len(nums) == 0:
      return -1
    if len(nums) == 1:
      if nums[0] == target:
        return 0
      else:
        return -1
    left, right = 0, len(nums) - 1
    while left < right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      # 分岐点がある場合
      if nums[mid] > nums[right]:
        if target >= nums[left] and target <= nums[mid]:
          right = mid
        else:
          left = mid + 1
      # 分岐点がない場合
      else:
        if nums[mid] < target and target<=nums[right]:
          left = mid + 1
        else:
          right = mid
    if nums[left] == target:
      return left
    else:
      return -1