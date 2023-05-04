# Linked listの問題
# 配列にアドレスを入れていき、一つずつ入れていく。最後だけlastとして管理。
class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    arr = []
    length = 0
    cur = head
    while cur != None:
      arr.append(cur)
      cur = cur.next
      length += 1
    left, right = 0, length - 1
    last = head
    while left < right:
      arr[left].next = arr[right]
      left += 1
      if left == right:
        last = arr[right]
        break
      arr[right].next = arr[left]
      right -= 1
      last = arr[left]
    if last:
      last.next = None