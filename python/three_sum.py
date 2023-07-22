from utils.benchmark import BenchmarkSummmary
import time
from math import factorial
from typing import List
from itertools import product, combinations
from collections import namedtuple

class Solution:

    Point = namedtuple("Point", ["x", "y"])
    class Path:
        def __init__(self, indices=set(), weights=[]):
            self.indices = indices
            self.weights = weights

        def __len__(self):
            return len(self.nums)

        def append_if_reachable(self, pt):
            if pt.x not in self.indices:
                ret = self.__class__(indices=self.indices.copy(), weights=self.weights + [pt.y])
                ret.indices.add(pt.x)
                return ret
            else:
                return None

    def __init__(self):
        self.benchmark = BenchmarkSummmary(separator="_")
        self.benchmark.add_computed("time_loop", "time_sort", time_total=sum, time_loopToSort=lambda l, s: l/s)
        self.benchmark.add_computed("size_len", size_predicted=lambda n: factorial(n)/(6*factorial(n-3)))

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Accepted: ~96 %ile time, ~5 %ile space

        My solution essentially implements the following standard Python tools from scratch:
            * bisect module: used to determine where to split an ordered sequence
            * collections.Counter: used to count repeated items in a sequence
                * basically the same thing I did, just cleaner and more concise
        """
        return self.threeSum_quadratic(nums)

    def threeSum_dfs(self, nums):
        N = len(nums)
        nums.sort()
        m, M = nums[0], nums[-1]
        visited = {}
        stack = list(nums)
        while len(stack) > 0:
            num = stack.pop()
    



    def threeSum_sort(self, nums):
        """TLE"""
        n = len(nums)
        trips = set()

        # O(n*lg(n))
        nums.sort()

        for left in range(n-2):
            l = nums[left]
            if (minDouble := l + nums[left+1]) > 0:
                break
            for right in range(left+2, n):
                r = nums[r]
                if minDouble + nums[right] > 0:
                    break
                for mid in range(left+1, right):
                    m = nums[mid]
                    if l + m + r > 0:
                        break
                    elif l + m + r == 0:
                        trips.add((l, m, r))
        return list(map(list, trips))

    def threeSum_quadratic(self, nums):
        N = len(nums)
        nums.sort()
        positive, values, trips = [], {}, set()
        for num in nums:
            values[num] = values.get(num, 0)
            values[num] += 1
        while len(nums) > 0 and nums[-1] > 0:
            positive.append(nums.pop())
        for n in nums:
            for p in positive:
                if (m := -(n+p)) in values:
                    if n <= m <= p:
                        if values[m] > 1 or n != m and m != p:
                            trips.add((n, m, p))
        if values.get(0, -1) >= 3:
            trips.add((0, 0, 0))
        return list(map(list, trips))

    def _threeSum_itertools(self, nums):
        """TLE"""
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

    def threeSum_benchmarked(self, nums: List[int]) -> List[List[int]]:
        start = time.time()
        n = len(nums)
        trips = set()

        # O(n*lg(n))
        nums.sort()
        sort_time = time.time()
        numConsidered = 0

        for left in range(n-2):
            l = nums[left]
            if (minDouble := l + nums[left+1]) > 0:
                break
            for right in range(left+2, n):
                r = nums[right]
                if minDouble + nums[right] > 0:
                    break
                for mid in range(left+1, right):
                    numConsidered += 1
                    m = nums[mid]
                    if l + m + r > 0:
                        break
                    elif l + m + r == 0:
                        trips.add((l, m, r))
        loop_time = time.time()
        st, lt, tt = sort_time - start, loop_time - sort_time, loop_time - start
        predicted = factorial(n)/(factorial(n-3)*6)
        return {
            "ans": list(map(list, trips)),
            "problem_size": {
                "len": len(nums),
                "range": (nums[0], nums[-1])
            },
            "time": {
                "sort": st,
                "loop": lt,
                "total": tt,
                "sort:loop": st/lt,
                "sort:total": st/tt,
                "loop:total": lt/tt,
            },
            "loop": {
                "size": numConsidered,
                "predicted": predicted,
                "size:predicted": numConsidered/predicted,
                "size:n": numConsidered/n,
                "size:n**2": numConsidered/n**2,
                "size:n**3": numConsidered/n**3
            }
        }
