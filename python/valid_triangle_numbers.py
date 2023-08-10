"""
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Note that repetitions are allowed, i.e., if an element of the array occurs with multiplicity > 1, then all the associated triple should be counted with the same multiplicity.
"""
from bisect import bisect_left, bisect_right

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        32.03 %ile runtime
        16.85 %ile memory
        """
        total = 0
        nums.sort()
        for i, x in enumerate(nums):
            for j in range(i+1, len(nums)):
                r = bisect_left(nums, x + nums[j], j)
                total += max(r - j - 1, 0)

        return total


