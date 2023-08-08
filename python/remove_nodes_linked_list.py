# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        94.69 %ile runtime
        63.69 %ile memory
        """
        maxima = [head]
        curr = head
        while curr is not None:
            while len(maxima) > 0 and curr.val > maxima[-1].val:
                maxima.pop()
            maxima.append(curr)
            curr = curr.next
        curr = maxima[0]
        for node in maxima[1:]:
            curr.next = node
            curr = node
        maxima[-1].next = None
        return maxima[0]
