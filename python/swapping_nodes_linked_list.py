"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    98.39 %ile runtime
    96.05 %ile memory
    """
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        leader = dummy
        for i in range(k):
            leader = leader.next
        first = leader
        while leader is not None:
            dummy, leader = dummy.next, leader.next
        first.val, dummy.val = dummy.val, first.val
        return head
