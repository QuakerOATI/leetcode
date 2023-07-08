from utils.test import test, given
from numpy import int32
import sys
import random

class Solution:
    MIN = -2**31
    MAX = 2**31 - 1

    def __init__(self):
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("error", RuntimeWarning)

    def reverse(self, x: int) -> int:
        ds = self.digits(x)
        ds.reverse()
        return self.reconstruct_32bit([ds[-1], *ds[:-1]])

    @classmethod
    def digits(cls, x):
        if x < 0:
            ret = cls.digits(-x)
            ret[0] = -1
            return ret
        d = [1]
        while x:
            d.append(x % 10)
            x //= 10
        return d

    @classmethod
    def reconstruct_int(cls, arr):
        x = 0
        while len(arr) > 1:
            x *= 10
            x += arr[0]*arr.pop()
        return x

    @classmethod
    def reconstruct_32bit(cls, arr):
        try:
            arr = list(map(int32, arr))
            ten = int32(10)
            x = int32(0)
            while len(arr) > 1:
                x *= ten
                x += arr[0]*arr.pop()
            return x
        except RuntimeWarning:
            return 0
    
    @classmethod
    @given(None, (random.randint, -2**31, 2**31-1))
    @test
    def test_reconstruct_int(cls, x):
        assert x == cls.reconstruct_32bit(cls.digits(x))

    @classmethod 
    @given(None, (random.randint, -2**31, 2**31-1))
    @test
    def test_reverse(cls, x):
        s = cls()
        ret = s.reverse(x)
        ds = s.digits(x)
        ds.reverse()
        real = s.reconstruct_int([ds[-1], *ds[:-1]])
        if real > s.MAX:
            assert ret == 0
        elif real < s.MIN:
            assert ret == 0
        else:
            assert ret == real
