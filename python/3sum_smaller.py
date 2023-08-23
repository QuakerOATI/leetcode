"""
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
"""


class Solution:

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        99.62 %ile runtime
        81.12 %ile memory
        """
        ret = 0
        nums.sort()
        n = len(nums)
        if n < 3:
            return 0
        for i in range(n - 2):
            x = nums[i]
            low, high = x + nums[i + 1] + nums[i + 2], x + nums[n -
                                                                1] + nums[n -
                                                                          2]
            if high < target:
                ret += (n - i - 1) * (n - i - 2) // 2
            elif low >= target:
                return ret
            else:
                l, r = i + 1, n - 1
                while l < r:
                    y, z = nums[l], nums[r]
                    if x + y + z < target:
                        ret += r - l
                        l += 1
                    else:
                        r -= 1
        return ret
