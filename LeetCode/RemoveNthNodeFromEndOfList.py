# LinkedListの問題
# 以下自力。解答は微妙。
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    length = 0
    cur = head
    while cur != None:
      cur = cur.next
      length += 1
    if length == 1:
      head = None
      return head
    if length == 2:
      if n == 1:
        head.next = None
      else:
        head = head.next
      return head
    dummy = head
    currNode = dummy
    if length - n == 0:
      dummy = dummy.next
    for i in range(length-1):
      if i != length-n-1:
        currNode = currNode.next
      else:
        tmp = currNode.next
        if tmp != None:
          currNode.next = tmp.next
          currNode = tmp.next
    return dummy
