from typing import List
from bisect import bisect_right


class Solution:

    def optimalSolution(self, target, nums):
        """There is one key point here and one useful trick:
        1. Once an optimal left-endpoint has been found for a given right-endpoint, all subsequent optimal left-endpoints must be equal to or to the right of it.
        2. The use of float("inf") as a value which always compares greater than any other.
        """
        left = 0
        curr_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0

    def minSubArrayLenBinarySearch(self, target, nums):
        """FINALLY accepted, but still kind of sucks"""
        if sum(nums) < target or len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1 if nums[0] >= target else 0
        best = len(nums)
        # Constructing sums with a comprehension was a sticking point here
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)
        for left in range(len(nums)):
            bp = bisect_right(sums, target, left + 1, len(nums) + 1) - 1
            if bp == len(nums) and target == sums[-1]:
                best = min(best, bp - left)
                break
            elif bp == len(nums) and target > sums[-1]:
                break
            elif sums[bp] == target:
                best = min(best, bp - left)
            else:
                best = min(best, bp - left + 1)
            target += nums[left]
        return best

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Recursive solution.  Exceeds memory limit."""
        Lt = self.minTerminalSubarrayLen(target, nums)
        if Lt == 0:
            return 0
        L = self.minSubArrayLen(target, nums[:-1])

        if L > 0:
            return min(L, Lt)
        else:
            return Lt

    def minTerminalSubarrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1 if nums[0] >= target else 0
        elif nums[-1] >= target:
            return 1
        elif (L := self.minTerminalSubarrayLen(target - nums[-1],
                                               nums[:-1])) > 0:
            return L + 1
        else:
            return 0

    def minSubArrayLenIterative(self, target: int, nums: List[int]) -> int:
        """TLE"""
        N = len(nums)
        A = nums.copy()
        for L in range(1, N):
            for i in range(N - L):
                A[i] += nums[i + L]
                if A[i] >= target:
                    return L
        return 0

    def minSubArrayLenGreedy(self, target: int, nums: List[int]) -> int:
        """This appears to simply not work."""
        from math import ceil
        S = sum(nums)
        if S < target:
            return 0
        ct = -1
        while S >= target and len(nums) > 0:
            ct += 1
            if len(nums) == 1:
                return 1
            if nums[0] == nums[-1]:
                print(f"**Degenerate case at index {ct}**")
                print(f"    nums[0] = nums[-1] = {nums[0]}")
                m = 0
                while 2 * m < len(nums) and nums[m] == nums[
                        len(nums) - m - 1] and S - (m + 1) * nums[0] >= target:
                    m += 1
                print(f"    Pruned off prefix and suffix of length {m}")
                print(f"        nums[m := {m}] = {nums[m]}")
                print(
                    f"        nums[{len(nums) - m - 1}] = {nums[len(nums) - m - 1]}"
                )
                if m == len(nums) - m - 1:
                    print(f"Case 1: m == len(nums) - m - 1")
                    if nums[m] < nums[0]:
                        print(f"        Case 1a: nums[m] < nums[0]")
                        if (T := S - m * nums[0] - nums[m]) >= target:
                            return ceil(target / nums[0])
                        else:
                            return m + 1
                    elif nums[m] >= target:
                        print(f"        Case 1b: nums[m] >= target")
                        return 1
                    else:
                        print(f"        Case 1c: nums[0] < nums[m] < target")
                        return 1 + ceil((target - nums[m]) / nums[0])
                elif m > len(nums) - m - 1:
                    print(f"Case 2: m > len(nums) - m - 1")
                    return ceil(target / nums[0])
                elif nums[m] < nums[len(nums) - m - 1]:
                    print(f"Case 3: nums[m] < nums[len(nums) - m - 1]")
                    S -= m * nums[0]
                    nums = nums[m:]
                else:
                    print(f"Case 4: nums[m] >= nums[len(nums) - m - 1]")
                    S -= m * nums[0]
                    nums = nums[:-m]

            if nums[0] > nums[-1]:
                S -= nums.pop()
            elif nums[0] < nums[-1]:
                S -= nums.pop(0)

        return len(nums) + 1
