"""
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

    For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.

Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 10**9 + 7.
"""
from typing import List
from math import factorial


def binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


class Solution:

    def numOfWays(self, nums: List[int]) -> int:
        """
        9.11 %ile runtime
        11.50 %ile memory
        """
        N = 10**9 + 7
        if len(nums) < 3:
            return 0
        lnums = list(enumerate(nums))

        def helper(j, m, M):
            if len(nums) - j < 3:
                return 1
            root = nums[j]
            if M - m < 3:
                return 1
            subtree = list(
                filter(lambda p: p[1] < M and p[1] > m, lnums[j + 1:]))
            L = [i for i, x in subtree if x < root]
            R = [k for k, y in subtree if y > root]
            numLeft = helper(min(L), m, root) if len(L) > 0 else 0
            numRight = helper(min(R), root, M) if len(R) > 0 else 0
            if numLeft == 0:
                return numRight if numRight != 0 else 1
            elif numRight == 0:
                return numLeft
            return numLeft * numRight * binom(len(L) + len(R), len(L)) % N

        return helper(0, 0, len(nums) + 1) % N - 1
