from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if (N := len(nums)) < 2*k + 1:
            return [-1]*N
        ans = [-1 for _ in range(k)]
        S = sum(nums[:2*k]) + nums[-1]
        for j in range(k, len(nums) - k):
            S += nums[j+k] - nums[j-k-1]
            ans.append(S//(2*k+1))
        ans.extend([-1 for _ in range(k)])
        return ans


    def generate_testcase(self):
        ...

    def brute_force(self, nums, k):
        ans = []
        for i, n in enumerate(nums):
            if i < k or i >= len(nums) - k:
                ans.append(-1)
            else:
                ans.append(sum(nums[i-k:i+k+1])//(2*k+1))
        return ans
