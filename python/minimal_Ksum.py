class Solution:
    """
    You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.

Return the sum of the k integers appended to nums.

Accepted, but definitely not optimal (see appended optimal solution).
    """

    def minimalKSum(self, nums: List[int], k: int) -> int:
        T = 0
        for i, num in enumerate(L := sorted(nums + [0])):
            if i == len(L) - 1:
                break
            if k <= 0:
                break
            if L[i + 1] <= 0:
                continue
            if num == L[i + 1] or num == L[i + 1] - 1:
                continue
            sz = min(k, L[i + 1] - max(0, num) - 1)
            T += ((2 * L[i] + sz + 1) * sz) // 2
            k -= sz
        if k > 0:
            l = max(0, L[-1])
            T += ((l + 1 + l + k) * k) // 2
        return T
