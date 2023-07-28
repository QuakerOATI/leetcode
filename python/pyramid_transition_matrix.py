"""
You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.

To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

    For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.

You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.
"""

from itertools import product
from typing import List
from collections import defaultdict


class Solution:

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        return self.pyramidTransitionRecursive(bottom, allowed,
                                               {s[:2]
                                                for s in allowed})

    def pyramidTransitionRecursive(self, bottom, allowed, memo):
        """Top-down memoized recursion"""
        if len(bottom) < 2:
            return False
        if bottom not in memo:
            for s in product(*map(
                    lambda p: (a[-1] for a in allowed if a.startswith("".join(
                        p))), zip(bottom, bottom[1:]))):
                if self.pyramidTransitionRecursive("".join(s), allowed, memo):
                    memo.add(bottom)
                    return True
        return bottom in memo

    def pyramidTransitionDP(self, bottom, allowed):
        """Memory limit exceeded"""
        dp = defaultdict(set)
        for a in allowed:
            dp[a[:2]].add(a[-1])

        def helper(s):
            if len(dp[s]) > 0:
                return True
            for L in range(2, len(s)):
                if not helper(s[:L]):
                    return False
            for x, c in product(dp[s[:-1]], dp[s[-2:]]):
                if helper(x + c):
                    dp[s].add(x + c)
            return len(dp[s]) > 0

        return helper(bottom)
