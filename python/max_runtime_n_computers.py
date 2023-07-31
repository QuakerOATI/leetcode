"""
An attempt to solve Maximum Running Time of N Computers
after the obvious priority-queue-based approach failed 
in javascript.
"""
from typing import List
import heapq
from bisect import bisect_right, bisect_left
from collections import Counter

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        return self.maxRunTimeBinarySearch(n, batteries)

    def maxRunTimeCounter(self, n: int, batteries: List[int]) -> int:
        """TLE"""
        c = Counter({i: b for i, b in enumerate(batteries)})
        m = 0
        while True:
            used = c.most_common(n)
            if used[-1][1] <= 0:
                break
            c.subtract([b[0] for b in used])
            m += 1
        return m

    def maxRunTimeHeap(self, n: int, batteries: List[int]) -> int:
        """TLE"""
        batteries = [-b for b in batteries]
        heapq.heapify(batteries)
        count = 0
        while (len(batteries) >= n):
            used = []
            for _ in range(n):
                b = heapq.heappop(batteries)
                if (b >= 0):
                    return count
                used.append(b)
            for bat in used:
                if bat < -1:
                    heapq.heappush(batteries, bat+1)
            count += 1
        return count

    def maxRunTimeBinarySearch(self, n: int, batteries: List[int]) -> int:
        """
        Total power available = sum([x for x in batteries if x < ans else ans])
        Total power consumed = n*ans
        ==> sum([x for x in batteries if x < ans else ans]) >= n*ans
        """

        def is_possible(t):
            return sum([b if b <= t else t for b in batteries]) >= n*t

        # First, do an exponential search to find range
        l, r = 0, max(batteries)
        while is_possible(r):
            l, r = r, 2*r

        # Now do a binary search on the range we just found
        while r - l > 1:
            m = (l + r)//2
            if is_possible(m):
                l = m
            else:
                r = m
        return r if is_possible(r) else l
