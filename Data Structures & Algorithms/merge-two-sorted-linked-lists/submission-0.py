# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
                temp.next = None
                current.next = temp
                current = current.next
            else:
                temp = list2
                list2 = list2.next
                temp.next = None
                current.next = temp
                current = current.next
        
        while list1:
            temp = list1
            list1 = list1.next
            temp.next = None
            current.next = temp
            current = current.next
        
        while list2:
            temp = list2
            list2 = list2.next
            temp.next = None
            current.next = temp
            current = current.next
        
        return dummy.next