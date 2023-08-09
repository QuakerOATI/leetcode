"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Idea: minimize (distance remaining) - (max jump size) at each step
        (len(nums) - 1) - j - nums[j]

        40.68 %ile runtime
        78.49 %ile memory
        """
        loc = []
        for i, n in enumerate(nums):
            if len(loc) < 2 or nums[loc[-2]] < i - loc[-2]:
                loc.append(i)
                continue
            loc[-1] = max(loc[-1], i, key=lambda j: nums[j] + j)
        return len(loc) - 1
