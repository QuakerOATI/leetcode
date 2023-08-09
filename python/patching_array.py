"""
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.
"""
from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    """
    70.59 %ile runtime
    28.43 %ile memory
    """
    def minPatches(self, nums: List[int], n: int) -> int:
        jl, jr, N = 0, 0, 0
        patch = 0
        while N < n:
            print(f"N = {N}, (jl, jr) = {(jl, jr)}, patch = {patch}")
            jl, jr = bisect_left(nums, N+1, jl), bisect_right(nums, N+1, jr)
            print(f"    New (jl, jr) = {(jl, jr)}")
            print(f"        {nums[:jl]} {nums[jl:jr+1]} {nums[jr+1:]}")
            if jr > jl:
                N = (1 + jr - jl)*N + (jr - jl)     # we get this "for free"
                print(f"    Free: N --> {1 + jr - jl}*N + {jr - jl} = {N}")
            else:
                patch += 1
                print(f"    Patching {N+1}")                 
                N = 2*N + 1
                print(f"        N --> 2*N + 1 = {N}")           
            jl, jr = jr, bisect_right(nums, N, jr)
            print(f"    After patch: (jl, jr) = {(jl, jr)}")
            while jr > jl and N < n:
                N += sum(nums[jl:jr])
                print(f"        Adding N --> N + {sum(nums[jl:jr])} = {N}")
                jl, jr = jr, bisect_right(nums, N, jr)

        return patch
