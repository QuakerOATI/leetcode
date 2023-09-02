"""
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

SOLUTION:
    l := leftmost endpoint among all endpoints of flipped intervals
    l == 0 necessarily
    Base case <- l == len(nums) - k

"""

from collections import deque


class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        """
        71.90 %ile runtime
        19.83 %ile memory
        """
        frame, N, ct = deque(), len(nums), 0
        for i, b in enumerate(nums):
            while len(frame) > 0 and i - frame[0] >= k:
                frame.popleft()
                ct += 1
            if len(frame) % 2 == b:
                if N - i >= k:
                    frame.append(i)
                else:
                    return -1
        return ct + len(frame)
