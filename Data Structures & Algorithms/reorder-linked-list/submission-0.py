
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        current = second
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        first, second = head, prev
        current = dummy
        while first and second:
            current.next = first
            first = first.next
            current = current.next
            current.next = second
            second = second.next
            current = current.next
            current.next = None
            

        if first and not second:
            current.next = first
        elif second and not first:
            current.next = second
