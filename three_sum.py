from typing import List
from itertools import product, combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

    def threeSum_sort(self, nums):
        """TLE"""
        n = len(nums)
        trips = set()

        # O(n*lg(n))
        nums.sort()

        for left in range(n-2):
            for right in range(n-1, left+1, -1):
                for mid in range(left+1, right):
                    if (l := nums[left]) + (m := nums[mid]) + (r := nums[right]) > 0:
                        break
                    elif l + m + r == 0:
                        trips.add((l, m, r))
        return list(map(list, trips))

    def threeSum_quadratic(self, nums):
        N = len(nums)
        vals, pairs, trips = {}, {}, set()
        for i in range(N):
            for j in range(i+1, N):
                x, y = nums[i], nums[j]
                vals[x] = vals.get(x, set())
                vals[x].add(i)
                s = x+y
                pairs[s] = pairs.get(s, set())
                pairs[s].add((min(x, y), max(x, y)))
        for s, ps in pairs.items():
            if -s in vals:
                for x, y in ps:
                    for k in vals[-s]:
                        trip = [x, y, -s]
                        trip.sort()
                        trips.add(tuple(trip))
        return list(map(list, trips))

    def _threeSum_itertools(self, nums):
        trips = set()
        for triplet in combinations(nums, 3):
            triplet = list(triplet)
            triplet.sort()
            if sum(triplet) == 0:
                trips.add(tuple(triplet))
        return list(map(list, trips))

    def _threeSum_mySolution(self, nums: List[int]) -> List[List[int]]:
        """O(n**3).  Time limit exceeded."""
        n = len(nums)
        
        trips = set()
        doubles = {}

        # O(n**2)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         doubles[i, j] = nums[i] + nums[j]

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    xs = [nums[i], nums[j], nums[k]]
                    xs.sort()
                    if sum(xs) == 0:
                        trips.add(tuple(xs))
        return list(map(list, trips))
