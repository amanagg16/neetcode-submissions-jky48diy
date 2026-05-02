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
            pl = pl.next
            l = l.next
        
        r, nr = head, head.next
        for i in range(right-1):
            nr = nr.next
            r = r.next
        
        prev = None
        current = l
        while current != nr:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        pl.next = prev
        current = prev
        while current.next != None:
            current = current.next
        
        current.next = nr
        

        return dummy.next