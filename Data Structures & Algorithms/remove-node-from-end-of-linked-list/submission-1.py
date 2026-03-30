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
        if not prev: return head.next
        prev.next = current.next
        return head