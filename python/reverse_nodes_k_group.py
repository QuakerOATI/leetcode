"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode],
                      k: int) -> Optional[ListNode]:
        """
        89.79 %ile runtime
        74.60 %ile memory
        """

        def advanceK(node, num):
            for i in range(num):
                if node is None:
                    return None
                node = node.next
            return node

        def reverseMiddle(prev, tail):
            first = prev.next
            ret = first
            while tail is not first:
                prev.next = first.next
                first.next = tail.next
                tail.next = first
                first = prev.next
            return ret

        dummy = ListNode(None, head)
        prev = dummy
        tail = advanceK(dummy, k)
        while tail is not None:
            prev = reverseMiddle(prev, tail)
            tail = advanceK(prev, k)

        return dummy.next
