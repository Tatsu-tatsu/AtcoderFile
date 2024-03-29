class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
      return None
    prevNode, currNode = head, head
    while currNode != None:
      if prevNode == currNode:
        currNode = currNode.next
        prevNode.next = None
      else:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    return prevNode
        