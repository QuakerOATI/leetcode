class Solution:
    """
    Given an integer array nums and an integer k, return the maximum length of a
subarray that sums to k.
    If there is not one, return 0 instead.
    """

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        psums = {}
        S = 0
        best = -float("inf")
        for i, num in enumerate(nums):
            S += num
            psums.setdefault(S, i)
            if S == k:
                best = max(best, i + 1)
            if S - k in psums:
                best = max(i - psums[S - k], best)
        return best if best != -float("inf") else 0
