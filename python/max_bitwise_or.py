from functools import reduce


class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:

        def helper(nums):

            nums.sort()
            tot = reduce(lambda a, b: a | b, nums, 0)
            num_subsets, subtot = helper(nums[:-1])

            return num_subsets, tot

        #
        # c = Counter(n.bit_length() for n in nums)
        # nums.sort()
        # bit_lengths = [n.bit_length() for n in nums]
        # j = bisect_left(bit_lengths, bit_lengths[-1] - 1)
