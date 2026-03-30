# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heapify, heappush, heappop

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        

        heap = []
        dummy = ListNode(0)
        current = dummy

        for index, head in enumerate(lists):
            if head:
                heap.append((head.val, index, head)) # very important...we need head.val to operate in heap, index so that we can get the next node in this linkedlist and head so that we can append this head to the end of the resultant linked list
                # also if head.val is same...then lower index value will be chosen...this is how heaps work...if first value is same then second value is used to break the tie
        
        heapify(heap)

        while heap:
            _ , index, node = heappop(heap)
            current.next = node
            current = node
            node = node.next
            current.next = None

            if node:
                heappush(heap, (node.val, index, node))

        return dummy.next