class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    currNode = dummy
    while list1 != None and list2 != None:
      if list1.val <= list2.val:
        currNode.next = list1
        list1 = list1.next
      else:
        currNode.next = list2
        list2 = list2.next
      currNode = currNode.next
    if list1 == None:
      currNode.next = list2
    else:
      currNode.next = list1
    return dummy.next

    # if list1.val <= list2.val:
    #   head = list1
    #   list1 = list1.next
    # else:
    #   head = list2
    #   list2 = list2.next
    # currNode = head
    # while list1 != None and list2 != None:
    #   if list1.val <= list2.val:
    #     currNode.next = list1
    #     list1 = list1.next
    #   else:
    #     currNode.next = list2
    #     list2 = list2.next
    #   currNode = currNode.next
    # if list1 == None:
    #   currNode.next = list2
    # else:
    #   currNode.next = list1
    # return head