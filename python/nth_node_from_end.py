class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Accepted, only beats about half the other solutions in runtime though

    Very clever optimization: Add a dummy node at the head of the list to avoid the null checks
    """

    def removeNthFromEnd(self, head, n):
        front, back = head, head
        for _ in range(n):
            front = front.next
        if front is None:
            return head.next
        front = front.next
        while front is not None:
            front = front.next
            back = back.next
        back.next = back.next.next
        return head
