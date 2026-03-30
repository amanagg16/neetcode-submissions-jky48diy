# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        def reverse(head, prev):

            if not head:
                return prev

            temp = head.next
            head.next = prev
            prev = head
            head = temp
            return reverse(head, prev)

        return reverse(head, prev)

