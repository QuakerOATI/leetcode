"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""


class Solution:

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        """
        99.81 %ile runtime
        55.28 %ile memory
        """

        def helper(num, cs, seq):
            if num == 0:
                yield list(seq)
            for i, c in enumerate(cs):
                if c <= num:
                    seq.append(c)
                    yield from helper(num - c, cs[i:], seq)
                    seq.pop()

        candidates.sort(reverse=True)
        return list(helper(target, candidates, []))
