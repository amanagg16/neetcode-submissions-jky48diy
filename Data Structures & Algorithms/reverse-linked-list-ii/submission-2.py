# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0, head)

        pl, l = dummy, head
        for i in range(left-1):   
            pl, l = pl.next, l.next
        
        r, nr = head, head.next
        for i in range(right-1):
            nr, r = nr.next, r.next
        
        prev, current = None, l
        while current != nr:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        pl.next, current = prev, prev
        # while current.next != None:
        #     current = current.next
        
        # current.next = nr
        l.next = nr
        
        return dummy.next