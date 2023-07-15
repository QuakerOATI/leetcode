from typing import List
class Solution:
    MAX = 10**9
    MIN = 10**9
    def __init__(self):
        self.num_bits = self.MAX.bit_length() + 2
    def majorityElement(self, nums: List[int]) -> int:
        bits = [0 for i in range(self.num_bits)]
        N = len(nums)
        max_pos = 0
        for n in nums:
            if n < 0:
                bits[-1] += 1
            for pos in range(self.num_bits):
                if n == 0:
                    break
                if pos > max_pos:
                    max_pos = pos
                bits[pos] += int(n % 2 == 1)
                n >>= 1
        maj = 0
        for b in bits[max_pos::-1]:
            maj <<= 1
            maj += int(b > N//2)
        if bits[-1] > N//2:
            maj *= -1
        return maj
