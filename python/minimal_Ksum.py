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

    def optimalKSum(self, nums, k):
        """Takeaways:
        1. Technique for getting a "sorted set" (i.e., remove duplicates and also order the elements)
        2. Crux move: keep track of the sum of all array elements <= k as you iterate
        """
        nums = list(set(nums))
        nums.sort()
        last_term = k
        removable_sum = 0
        for num in nums:
            if (num <= last_term):
                last_term += 1
                removable_sum += num
            else:
                break
        somme = (last_term * (1 + last_term) / 2) - removable_sum
        return int(somme)
