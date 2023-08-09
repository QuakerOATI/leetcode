"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Idea: if n is reachable, then so is k for all k < n.
            Proof: induction
        WLOG, we can therefore take the last jump to be as large as possible.

        94.29 %ile runtime
        68.52 %ile memory
        """
        l = 0
        for i, j in enumerate(reversed(nums)):
            if j >= i - l:
                l = i
        return l == len(nums) - 1
