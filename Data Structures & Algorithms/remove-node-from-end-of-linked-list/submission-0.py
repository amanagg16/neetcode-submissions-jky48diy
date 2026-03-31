# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, current, offset = None, head, head
        
        while n:
            offset = offset.next
            n-=1
        
        while offset:
            prev = current
            current = current.next
            offset = offset.next
        if not prev: return prev
        prev.next = current.next
        return head