# coding: utf-8
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            if ny <= 0:
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                nums = list(xs[lx:rx+1])
                for y in ys:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx+my+1
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                
        
from typing import List
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            if ny <= 0:
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                nums = list(xs[lx:rx+1])
                for y in ys:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx+my+1
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                
        
def testcase(size=100):
    nx = randint(0, size)
    ny = size - nx
    xs = sorted([randint(-1000, 1000) for _ in range(nx)])
    ys = sorted([randint(-1000, 1000) for _ in range(ny)])
    k = randint(0, size-1)
    ans = sorted(xs + ys)[k:k+2]
    return ((xs, ys, k), ans)
    
testcase()
from random import choice, randint, choices
testcase()
def test(size=100):
    tc = testcase()
    s = Solution()
    ret = s.find_kth_pair(*tc[0])
    if ret != tc[1]:
        print(f"Oh no!  Test failed")
        print(f"    expected:{tc[1].rjust(50)}")
        print(f"    returned:{ret.rjust(50)}")
    else:
        print("Pass")
    return tc
    
test()
def test(size=100):
    tc = testcase()
    s = Solution()
    ret = s.find_kth_pair(*tc[0])
    if ret != tc[1]:
        print(f"Oh no!  Test failed")
        print(f"    expected:{str(tc[1]).rjust(50)}")
        print(f"    returned:{str(ret).rjust(50)}")
    else:
        print("Pass")
    return tc
    
tc = test()
xs, ys, k = tc[0]
k
xs
ys
sorted(xs + ys)[k:k+2]
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            if ny <= 0:
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                nums = list(xs[lx:rx+1])
                for y in ys:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx+my+1
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
                
        
tc = test()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
          
            
            if ny <= 0:
                print(f"Base case: ny <= 0")
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                nums = list(xs[lx:rx+1])
                for y in ys:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx+my+1
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
                    
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys)
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys)
                nums = list(xs[lx:rx+1])
                for y in ys:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating: mx = {mx}, pivot = {pivot}", lx, ly, rx, ry, xs, ys)
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx+my+1
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys):
        print(msg)
        if rx >= lx:
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
            
tc = test()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k)
                nums = list(xs[lx:rx+1])
                for y in ys:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating: mx = {mx}, pivot = {pivot}", lx, ly, rx, ry, xs, ys, k)
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx+my+1
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k):
        print(msg)
        print(f"              k = {k}")
        if rx >= lx:
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
            
test()
tc = test()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k)
                nums = list(xs[lx:rx+1])
                for y in ys:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating: mx = {mx}, pivot = {pivot}", lx, ly, rx, ry, xs, ys, k)
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx + my - lx - ly + 1
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k):
        print(msg)
        print(f"              k = {k}")
        if rx >= lx:
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
            
tc = test()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k)
                nums = list(xs[lx:rx+1])
                for y in ys:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating: mx = {mx}, pivot = {pivot}", lx, ly, rx, ry, xs, ys, k)
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx + my - lx - ly + 1
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k):
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"      expected = {sorted(nums)[k]}")
        
tc = test()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k)
                nums = list(xs[lx:rx+1])
                for y in ys:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, "mx - lx =".rjust(17) + f" {mx - lx}", f"pivot =".rjust(17) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx + my - lx - ly + 1
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, *msgs):
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k)
                nums = list(xs[lx:rx+1])
                for y in ys:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx + my - lx - ly + 1
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, *msgs):
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test()
tc = test()
tc = test()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx + my - lx - ly + 1
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, *msgs):
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:rx+1], ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, *msgs):
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                if my == 0:
                    return xs[lx+k:lx+k+2]
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, *msgs):
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ...

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, *msgs):
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
tc = test()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        if len(nums1) + len(num2) % 2 == 1:
            return float(pair[0])
        else:
            return sum(pair)/2

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, *msgs):
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
from statistics import median
def test_median(size=100):
    tc = testcase(size=size)
    s = Solution()
    pair = s.find_kth_pair(*tc[0])
    found = s.findMedianSortedArrays(*tc[0][:2])
    expected = median(sum(*tc[0][:2]))
    if found != expected:
        print(f"Oh no!  Test failed")
        print(indent + "expected = ".rjust(25) + str(expected))
        print(indent + "found = ".rjust(25) + str(found))
        print(indent + "pair = ".rjust(25) + str(pair))
    else:
        print("You passed, son")
        
from statistics import median
def test_median(size=100):
    tc = testcase(size=size)
    s = Solution()
    pair = s.find_kth_pair(*tc[0])
    found = s.findMedianSortedArrays(*tc[0][:2])
    expected = median(sum(*tc[0][:2]))
    if found != expected:
        print(f"Oh no!  Test failed")
        print(indent + "expected = ".rjust(25) + str(expected))
        print(indent + "found = ".rjust(25) + str(found))
        print(indent + "pair = ".rjust(25) + str(pair))
    else:
        print("You passed, son")
    return tc
    
tc = test_median()
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        if len(nums1) + len(nums2) % 2 == 1:
            return float(pair[0])
        else:
            return sum(pair)/2

    def find_kth_pair(self, xs, ys, k):
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, *msgs):
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test_median()
tc[0][:2]
sum(tc[0][:2])
tc[0][0] + tc[0][1]
from statistics import median
def test_median(size=100):
    tc = testcase(size=size)
    s = Solution()
    pair = s.find_kth_pair(*tc[0])
    found = s.findMedianSortedArrays(*tc[0][:2])
    expected = median(tc[0][0] + tc[0][1])
    if found != expected:
        print(f"Oh no!  Test failed")
        print(indent + "expected = ".rjust(25) + str(expected))
        print(indent + "found = ".rjust(25) + str(found))
        print(indent + "pair = ".rjust(25) + str(pair))
    else:
        print("You passed, son")
    return tc
    
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
tc = test_median()
from statistics import median
def test_median(size=100, tc=None):
    if tc is None:
        tc = testcase(size=size)
    s = Solution()
    pair = s.find_kth_pair(*tc[0])
    found = s.findMedianSortedArrays(*tc[0][:2])
    expected = median(tc[0][0] + tc[0][1])
    if found != expected:
        print(f"Oh no!  Test failed")
        print(indent + "expected = ".rjust(25) + str(expected))
        print(indent + "found = ".rjust(25) + str(found))
        print(indent + "pair = ".rjust(25) + str(pair))
    else:
        print("You passed, son")
    return tc
    
tc = test_median(tc=(([1, 3], [2]), 0))
tc = test_median(tc=(([1, 3], [2], 0), 0))
from statistics import median
def test_median(size=100, tc=None):
    indent = "    "
    if tc is None:
        tc = testcase(size=size)
    s = Solution()
    pair = s.find_kth_pair(*tc[0])
    found = s.findMedianSortedArrays(*tc[0][:2])
    expected = median(tc[0][0] + tc[0][1])
    if found != expected:
        print(f"Oh no!  Test failed")
        print(indent + "expected = ".rjust(25) + str(expected))
        print(indent + "found = ".rjust(25) + str(found))
        print(indent + "pair = ".rjust(25) + str(pair))
    else:
        print("You passed, son")
    return tc
    
tc = test_median(tc=(([1, 3], [2], 0), 0))
from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        if len(nums1) + len(nums2) % 2 == 1:
            return float(pair[0])
        else:
            return sum(pair)/2

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, x_o, y_o, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, x_o, y_o, *msgs):
        if xs != x_o or ys != y_o:
            print(f"=== MUTATION ALERT ===")
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test_median(tc=(([1, 3], [2], 0), 0))
from bisect import bisect_right

class Solution:
    indent = "    "
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        print(f"Found median")
        print(indent + f"pair: {pair}")
        if len(nums1) + len(nums2) % 2 == 1:
            print(indent + f"Case ODD --> median = {float(pair[0])}")
            return float(pair[0])
        else:
            print(indent + f"Case EVEN --> median = {sum(pair/2.0)}")
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, x_o, y_o, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, x_o, y_o, *msgs):
        if xs != x_o or ys != y_o:
            print(f"=== MUTATION ALERT ===")
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test_median(tc=(([1, 3], [2], 0), 0))
from bisect import bisect_right

class Solution:
    indent = "    "
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        print(f"Found median")
        print(self.indent + f"pair: {pair}")
        if len(nums1) + len(nums2) % 2 == 1:
            print(self.indent + f"Case ODD --> median = {float(pair[0])}")
            return float(pair[0])
        else:
            print(self.indent + f"Case EVEN --> median = {sum(pair/2.0)}")
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, x_o, y_o, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, x_o, y_o, *msgs):
        if xs != x_o or ys != y_o:
            print(f"=== MUTATION ALERT ===")
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test_median(tc=(([1, 3], [2], 0), 0))
from bisect import bisect_right

class Solution:
    indent = "    "
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        print(f"Found median")
        print(self.indent + f"pair: {pair}")
        if len(nums1) + len(nums2) % 2 == 1:
            print(self.indent + f"Case ODD --> median = {float(pair[0])}")
            return float(pair[0])
        else:
            print(self.indent + f"Case EVEN --> median = {sum(pair)/2.0}")
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, x_o, y_o, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, x_o, y_o, *msgs):
        if xs != x_o or ys != y_o:
            print(f"=== MUTATION ALERT ===")
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test_median(tc=(([1, 3], [2], 0), 0))
from bisect import bisect_right

class Solution:
    indent = "    "
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x_o = sorted(nums1)
        y_o = sorted(nums2)
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        print(f"Found median")
        if x_o != nums1 or y_o != nums2:
            print(indent + f"MUTATION ALERT:")
            print(2*indent + f"xs = {nums1}")
            print(2*indent + f"  vs {x_o}")
            print(2*indent + f"ys = {nums2}")
            print(2*indent + f"  vs {y_o}")
        print(self.indent + f"pair: {pair}")
        if len(nums1) + len(nums2) % 2 == 1:
            print(self.indent + f"Case ODD --> median = {float(pair[0])}")
            return float(pair[0])
        else:
            print(self.indent + f"Case EVEN --> median = {sum(pair)/2.0}")
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, x_o, y_o, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, x_o, y_o, *msgs):
        if xs != x_o or ys != y_o:
            print(f"=== MUTATION ALERT ===")
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test_median(tc=(([1, 3], [2], 0), 0))
from bisect import bisect_right

class Solution:
    indent = "    "
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x_o = sorted(nums1)
        y_o = sorted(nums2)
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        print(f"Found median")
        if x_o != nums1 or y_o != nums2:
            print(indent + f"=== MUTATION ALERT ===")
        print(2*indent + f"xs = {nums1}")
        print(2*indent + f"  vs {x_o}")
        print(2*indent + f"ys = {nums2}")
        print(2*indent + f"  vs {y_o}")
        print(self.indent + f"pair: {pair}")
        if len(nums1) + len(nums2) % 2 == 1:
            print(self.indent + f"Case ODD --> median = {float(pair[0])}")
            return float(pair[0])
        else:
            print(self.indent + f"Case EVEN --> median = {sum(pair)/2.0}")
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, x_o, y_o, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, x_o, y_o, *msgs):
        if xs != x_o or ys != y_o:
            print(f"=== MUTATION ALERT ===")
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test_median(tc=(([1, 3], [2], 0), 0))
from bisect import bisect_right

class Solution:
    indent = "    "
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x_o = sorted(nums1)
        y_o = sorted(nums2)
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        print(f"Found median")
        if x_o != nums1 or y_o != nums2:
            print(self.indent + f"=== MUTATION ALERT ===")
        print(2*self.indent + f"xs = {nums1}")
        print(2*self.indent + f"  vs {x_o}")
        print(2*self.indent + f"ys = {nums2}")
        print(2*self.indent + f"  vs {y_o}")
        print(self.indent + f"pair: {pair}")
        if len(nums1) + len(nums2) % 2 == 1:
            print(self.indent + f"Case ODD --> median = {float(pair[0])}")
            return float(pair[0])
        else:
            print(self.indent + f"Case EVEN --> median = {sum(pair)/2.0}")
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, x_o, y_o, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, x_o, y_o, *msgs):
        if xs != x_o or ys != y_o:
            print(f"=== MUTATION ALERT ===")
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test_median(tc=(([1, 3], [2], 0), 0))
from bisect import bisect_right

class Solution:
    indent = "    "
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x_o = sorted(nums1)
        y_o = sorted(nums2)
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        print(f"Found median")
        if x_o != nums1 or y_o != nums2:
            print(self.indent + f"=== MUTATION ALERT ===")
        print(2*self.indent + f"xs = {nums1}")
        print(2*self.indent + f"  vs {x_o}")
        print(2*self.indent + f"ys = {nums2}")
        print(2*self.indent + f"  vs {y_o}")
        print(self.indent + f"pair: {pair}")
        if (len(nums1) + len(nums2)) % 2 == 1:
            print(self.indent + f"Case ODD --> median = {float(pair[0])}")
            return float(pair[0])
        else:
            print(self.indent + f"Case EVEN --> median = {sum(pair)/2.0}")
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, x_o, y_o, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, x_o, y_o, *msgs):
        if xs != x_o or ys != y_o:
            print(f"=== MUTATION ALERT ===")
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
tc = test_median(tc=(([1, 3], [2], 0), 0))
def make_testcase(xs, ys):
    L = len(xs) + len(ys)
    k = L//2
    return ((xs, ys, k), sorted(xs+ys)[k:k+2])
    
tc = make_testcase(list(range(1, 4)), list(range(4, 11)))
tc = test_median(tc=tc)
l = [1, 2, 34]
l[2:]
l[3:]
l[3]
from bisect import bisect_right

class Solution:
    indent = "    "
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x_o = sorted(nums1)
        y_o = sorted(nums2)
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        print(f"Found median")
        if x_o != nums1 or y_o != nums2:
            print(self.indent + f"=== MUTATION ALERT ===")
        print(2*self.indent + f"xs = {nums1}")
        print(2*self.indent + f"  vs {x_o}")
        print(2*self.indent + f"ys = {nums2}")
        print(2*self.indent + f"  vs {y_o}")
        print(self.indent + f"pair: {pair}")
        if (len(nums1) + len(nums2)) % 2 == 1:
            print(self.indent + f"Case ODD --> median = {float(pair[0])}")
            return float(pair[0])
        else:
            print(self.indent + f"Case EVEN --> median = {sum(pair)/2.0}")
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                self.print_state("Base case: ny <= 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                self.print_state("Base case: ny + ny < 5", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                self.print_state("Base case: ny < 3", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                self.print_state("Base case: k + 2 == nx + ny", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                self.print_state("Base case: k == 0", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                self.print_state(f"Iterating:", lx, ly, rx, ry, xs, ys, k, x_o, y_o, "mx - lx =".rjust(13) + f" {mx - lx}", f"pivot =".rjust(13) + f" {pivot}")
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    self.print_state("Base case: k == nl - 1", lx, ly, rx, ry, xs, ys, k, x_o, y_o)
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                    if my < len(ys):
                        return sorted([pivot, xs[mx+1], ys[my]])[:2]
                    else:
                        print(self.indent + f"EXTRA TRICKY case reached: my >= len(ys)")
                        return [pivot, xs[mx+1]]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
    def print_state(self, msg, lx, ly, rx, ry, xs, ys, k, x_o, y_o, *msgs):
        if xs != x_o or ys != y_o:
            print(f"=== MUTATION ALERT ===")
        print(msg)
        print(f"              k = {k}")
        nums = []
        if rx >= lx:
            nums += list(xs[lx:rx+1])
            print(f"    xs[lx:rx+1] = {xs[lx:rx+1]}")
        if ry >= ly:
            nums += list(ys[ly:ry+1])
            print(f"    ys[ly:ry+1] = {ys[ly:ry+1]}")
        print(f"       expected = {sorted(nums)[k:k+2]}")
        for m in msgs:
            print(f"    {m}")
            
from statistics import median
from collections import namedtuple

def bulk_test_median(num_random_tests=1000, size=range(100, 5000), elems=range(-5000, 5000), *cases, **named_cases):
    ind = "    "
    failed = []
    s = Solution()
    MedianTestCase = namedtuple("MedianTestCase", ["xs", "ys", "expected"])
    def _random_test(sz):
        nx = randint(0, sz)
        xs = sorted([choice(elems) for _ in range(nx)])
        ys = sorted([choice(elems) for _ in range(sz-nx)])
        expected = median(xs + ys)
        return MedianTestCase(xs, ys, expected)
    def _test(s, tc, show_output=False, indent=ind):
        s.chatty(show_output, indent=indent)
        found = s.findMedianSortedArrays(tc.xs, tc.ys)
        if found != tc.expected:
            print(f"Oh no!  Test failed")
            print(indent + "expected = ".rjust(25) + str(tc.expected))
            print(indent + "found = ".rjust(25) + str(found))
        elif show_output:
            print("You passed, son")
        return found
    for name, c in named_cases.items():
        print(f"{name.upper()}:")
        _test(s, c, show_output=True, indent=2*ind)
    for i, c in enumerate(cases):
        print(f"NUMBERED TESTCASE: ({i})")
        _test(s, c, show_output=True, indent=2*ind)
    for _ in range(num_random_tests):
        tc = _random_test(choice(size))
        found = _test(s, tc)
        if found != tc.expected:
            failed.append(tc)
            print(f"RANDOM TEST FAILED:")
            _test(s, tc, show_output=True, indent=2*ind)
            
from bisect import bisect_right

class Solution:
    def chatty(self, isChatty, baseIndent=0):
        self._chatty = isChatty
        self._base_indent = baseIndent
    def print(self, msg=None, level=0, extra_defn_indent=0, **defns):
        if self._chatty:
            print(level*self.indent + self._base_indent + msg)
            for name, variable in defns.items():
                if len(name) >= self._max_varname_length:
                    self._max_varname_length = len(name) + 1
                print((level + extra_defn_indent)*self.indent + self._base_indent + f"{name} = ".rjust(self._max_varname_length) + str(variable))
    def define(self, header=None, ident=1, **kwargs):
        if header is not None:
            self.print(header, level=ident, extra_defn_indent=1, **kwargs)
        else:
            self.print(header, level=ident, extra_defn_indent=0, **kwargs)
    def __init__(self):
        self._chatty = True
        self.indent = "    
        self._max_varname_length = 15
        self._base_indent = ""
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x_o = sorted(nums1)
        y_o = sorted(nums2)
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        self.print(f"Found median")
        if x_o != nums1 or y_o != nums2:
            self.print(f"=== MUTATION ALERT ===", 1)
        if (len(nums1) + len(nums2)) % 2 == 1:
            self.define("Case OOD:", ident=1, median=float(pair[0]))
            return float(pair[0])
        else:
            self.define("Case EVEN:", level=1, median=sum(pair)/2.0)
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        def print_extended_state(header):
            self.define(header, ident=0, **{"lx": lx, "ly": ly, "rx": rx, "ry": ry, "xs": xs, "ys": ys, "k": k, "x_o": x_o, "y_o": y_o})
        def print_state(header, **defns):
            self.define(header, ident=0, **{"xs[lx:rx+1]": xs[lx:rx+1], "ys[ly:ry+1]": ys[ly:ry+1], "k": k, "expect": sorted(xs[lx:rx+1]+ys[ly:ry+1])[k]}, **defns)
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                print_state("Base case: ny <= 0")
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                print_state("Base case: nx + ny < 5")
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                print_state("Base case: ny < 3")
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                print_state("Base case: k + 2 == nx + ny")
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                print_state("Base case: k == 0")
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                print_state("Iterating:", **{"mx - lx": mx-lx, "pivot": pivot})
                
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    print_state("Base case: k == nl - 1")
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                    if my < len(ys):
                        return sorted([pivot, xs[mx+1], ys[my]])[:2]
                    else:
                        print_state("EXTRA TRICKY: my >= len(ys)")
                        return [pivot, xs[mx+1]]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
from bisect import bisect_right

class Solution:
    def chatty(self, isChatty, baseIndent=0):
        self._chatty = isChatty
        self._base_indent = baseIndent
    def print(self, msg=None, level=0, extra_defn_indent=0, **defns):
        if self._chatty:
            print(level*self.indent + self._base_indent + msg)
            for name, variable in defns.items():
                if len(name) >= self._max_varname_length:
                    self._max_varname_length = len(name) + 1
                print((level + extra_defn_indent)*self.indent + self._base_indent + f"{name} = ".rjust(self._max_varname_length) + str(variable))
    def define(self, header=None, ident=1, **kwargs):
        if header is not None:
            self.print(header, level=ident, extra_defn_indent=1, **kwargs)
        else:
            self.print(header, level=ident, extra_defn_indent=0, **kwargs)
    def __init__(self):
        self._chatty = True
        self.indent = "    "
        self._max_varname_length = 15
        self._base_indent = ""
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x_o = sorted(nums1)
        y_o = sorted(nums2)
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        self.print(f"Found median")
        if x_o != nums1 or y_o != nums2:
            self.print(f"=== MUTATION ALERT ===", 1)
        if (len(nums1) + len(nums2)) % 2 == 1:
            self.define("Case OOD:", ident=1, median=float(pair[0]))
            return float(pair[0])
        else:
            self.define("Case EVEN:", level=1, median=sum(pair)/2.0)
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        def print_extended_state(header):
            self.define(header, ident=0, **{"lx": lx, "ly": ly, "rx": rx, "ry": ry, "xs": xs, "ys": ys, "k": k, "x_o": x_o, "y_o": y_o})
        def print_state(header, **defns):
            self.define(header, ident=0, **{"xs[lx:rx+1]": xs[lx:rx+1], "ys[ly:ry+1]": ys[ly:ry+1], "k": k, "expect": sorted(xs[lx:rx+1]+ys[ly:ry+1])[k]}, **defns)
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                print_state("Base case: ny <= 0")
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                print_state("Base case: nx + ny < 5")
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                print_state("Base case: ny < 3")
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                print_state("Base case: k + 2 == nx + ny")
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                print_state("Base case: k == 0")
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                print_state("Iterating:", **{"mx - lx": mx-lx, "pivot": pivot})
                
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    print_state("Base case: k == nl - 1")
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                    if my < len(ys):
                        return sorted([pivot, xs[mx+1], ys[my]])[:2]
                    else:
                        print_state("EXTRA TRICKY: my >= len(ys)")
                        return [pivot, xs[mx+1]]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
                    
from statistics import median
from collections import namedtuple

def bulk_test_median(num_random_tests=1000, size=range(100, 5000), elems=range(-5000, 5000), *cases, **named_cases):
    ind = "    "
    failed = []
    s = Solution()
    MedianTestCase = namedtuple("MedianTestCase", ["xs", "ys", "expected"])
    def _random_test(sz):
        nx = randint(0, sz)
        xs = sorted([choice(elems) for _ in range(nx)])
        ys = sorted([choice(elems) for _ in range(sz-nx)])
        expected = median(xs + ys)
        return MedianTestCase(xs, ys, expected)
    def _test(s, tc, show_output=False, indent=ind):
        s.chatty(show_output, indent=indent)
        found = s.findMedianSortedArrays(tc.xs, tc.ys)
        if found != tc.expected:
            s.chatty(True, indent="")
            s.define("Oh no!  Test failed:", expected=tc.expected, found=found)
        else:
            s.print("You passed, son")
        return found
    for name, c in named_cases.items():
        print(f"{name.upper()}:")
        _test(s, c, show_output=True, indent=2*ind)
    for i, c in enumerate(cases):
        print(f"NUMBERED TESTCASE: ({i})")
        _test(s, c, show_output=True, indent=2*ind)
    for _ in range(num_random_tests):
        tc = _random_test(choice(size))
        found = _test(s, tc)
        if found != tc.expected:
            failed.append(tc)
            print(f"RANDOM TEST FAILED:")
            _test(s, tc, show_output=True, indent=2*ind)
    s.chatty(True, "")
    s.define("BULK TEST COMPLETE:", **{"tests run": num_tests, "tests failed": len(failed)})
    return failed
    
    
    
f = bulk_test_median()
from statistics import median
from collections import namedtuple

def bulk_test_median(num_random_tests=1000, size=range(100, 5000), elems=range(-5000, 5000), *cases, **named_cases):
    ind = "    "
    failed = []
    s = Solution()
    MedianTestCase = namedtuple("MedianTestCase", ["xs", "ys", "expected"])
    def _random_test(sz):
        nx = randint(0, sz)
        xs = sorted([choice(elems) for _ in range(nx)])
        ys = sorted([choice(elems) for _ in range(sz-nx)])
        expected = median(xs + ys)
        return MedianTestCase(xs, ys, expected)
    def _test(s, tc, show_output=False, indent=ind):
        s.chatty(show_output, indent=indent)
        found = s.findMedianSortedArrays(tc.xs, tc.ys)
        if found != tc.expected:
            s.chatty(True, ident="")
            s.define("Oh no!  Test failed:", expected=tc.expected, found=found)
        else:
            s.print("You passed, son")
        return found
    for name, c in named_cases.items():
        print(f"{name.upper()}:")
        _test(s, c, show_output=True, indent=2*ind)
    for i, c in enumerate(cases):
        print(f"NUMBERED TESTCASE: ({i})")
        _test(s, c, show_output=True, indent=2*ind)
    for _ in range(num_random_tests):
        tc = _random_test(choice(size))
        found = _test(s, tc)
        if found != tc.expected:
            failed.append(tc)
            print(f"RANDOM TEST FAILED:")
            _test(s, tc, show_output=True, indent=2*ind)
    s.chatty(True, "")
    s.define("BULK TEST COMPLETE:", **{"tests run": num_tests, "tests failed": len(failed)})
    return failed
    
f = bulk_test_median()
from statistics import median
from collections import namedtuple

def bulk_test_median(num_random_tests=1000, size=range(100, 5000), elems=range(-5000, 5000), *cases, **named_cases):
    ind = "    "
    failed = []
    s = Solution()
    MedianTestCase = namedtuple("MedianTestCase", ["xs", "ys", "expected"])
    def _random_test(sz):
        nx = randint(0, sz)
        xs = sorted([choice(elems) for _ in range(nx)])
        ys = sorted([choice(elems) for _ in range(sz-nx)])
        expected = median(xs + ys)
        return MedianTestCase(xs, ys, expected)
    def _test(s, tc, show_output=False, indent=ind):
        s.chatty(show_output, ident=indent)
        found = s.findMedianSortedArrays(tc.xs, tc.ys)
        if found != tc.expected:
            s.chatty(True, ident="")
            s.define("Oh no!  Test failed:", expected=tc.expected, found=found)
        else:
            s.print("You passed, son")
        return found
    for name, c in named_cases.items():
        print(f"{name.upper()}:")
        _test(s, c, show_output=True, indent=2*ind)
    for i, c in enumerate(cases):
        print(f"NUMBERED TESTCASE: ({i})")
        _test(s, c, show_output=True, indent=2*ind)
    for _ in range(num_random_tests):
        tc = _random_test(choice(size))
        found = _test(s, tc)
        if found != tc.expected:
            failed.append(tc)
            print(f"RANDOM TEST FAILED:")
            _test(s, tc, show_output=True, indent=2*ind)
    s.chatty(True, "")
    s.define("BULK TEST COMPLETE:", **{"tests run": num_tests, "tests failed": len(failed)})
    return failed
    
f = bulk_test_median()
from statistics import median
from collections import namedtuple

def bulk_test_median(num_random_tests=1000, size=range(100, 5000), elems=range(-5000, 5000), *cases, **named_cases):
    ind = "    "
    failed = []
    s = Solution()
    MedianTestCase = namedtuple("MedianTestCase", ["xs", "ys", "expected"])
    def _random_test(sz):
        nx = randint(0, sz)
        xs = sorted([choice(elems) for _ in range(nx)])
        ys = sorted([choice(elems) for _ in range(sz-nx)])
        expected = median(xs + ys)
        return MedianTestCase(xs, ys, expected)
    def _test(s, tc, show_output=False, indent=ind):
        s.chatty(show_output, indent)
        found = s.findMedianSortedArrays(tc.xs, tc.ys)
        if found != tc.expected:
            s.chatty(True, "")
            s.define("Oh no!  Test failed:", expected=tc.expected, found=found)
        else:
            s.print("You passed, son")
        return found
    for name, c in named_cases.items():
        print(f"{name.upper()}:")
        _test(s, c, show_output=True, indent=2*ind)
    for i, c in enumerate(cases):
        print(f"NUMBERED TESTCASE: ({i})")
        _test(s, c, show_output=True, indent=2*ind)
    for _ in range(num_random_tests):
        tc = _random_test(choice(size))
        found = _test(s, tc)
        if found != tc.expected:
            failed.append(tc)
            print(f"RANDOM TEST FAILED:")
            _test(s, tc, show_output=True, indent=2*ind)
    s.chatty(True, "")
    s.define("BULK TEST COMPLETE:", **{"tests run": num_tests, "tests failed": len(failed)})
    return failed
    
f = bulk_test_median()
from bisect import bisect_right

class Solution:
    def chatty(self, isChatty, baseIndent=0):
        self._chatty = isChatty
        self._base_indent = baseIndent
    def print(self, msg=None, level=0, extra_defn_indent=0, **defns):
        if self._chatty:
            print(level*self.indent + self._base_indent + msg)
            for name, variable in defns.items():
                if len(name) >= self._max_varname_length:
                    self._max_varname_length = len(name) + 1
                print((level + extra_defn_indent)*self.indent + self._base_indent + f"{name} = ".rjust(self._max_varname_length) + str(variable))
    def define(self, header=None, level=1, **kwargs):
        if header is not None:
            self.print(header, level=level, extra_defn_indent=1, **kwargs)
        else:
            self.print(header, level=level, extra_defn_indent=0, **kwargs)
    def __init__(self):
        self._chatty = True
        self.indent = "    "
        self._max_varname_length = 15
        self._base_indent = ""
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x_o = sorted(nums1)
        y_o = sorted(nums2)
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        self.print(f"Found median")
        if x_o != nums1 or y_o != nums2:
            self.print(f"=== MUTATION ALERT ===", 1)
        if (len(nums1) + len(nums2)) % 2 == 1:
            self.define("Case OOD:", level=1, median=float(pair[0]))
            return float(pair[0])
        else:
            self.define("Case EVEN:", level=1, median=sum(pair)/2.0)
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        def print_extended_state(header):
            self.define(header, level=0, **{"lx": lx, "ly": ly, "rx": rx, "ry": ry, "xs": xs, "ys": ys, "k": k, "x_o": x_o, "y_o": y_o})
        def print_state(header, **defns):
            self.define(header, level=0, **{"xs[lx:rx+1]": xs[lx:rx+1], "ys[ly:ry+1]": ys[ly:ry+1], "k": k, "expect": sorted(xs[lx:rx+1]+ys[ly:ry+1])[k]}, **defns)
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                print_state("Base case: ny <= 0")
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                print_state("Base case: nx + ny < 5")
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                print_state("Base case: ny < 3")
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                print_state("Base case: k + 2 == nx + ny")
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                print_state("Base case: k == 0")
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                print_state("Iterating:", **{"mx - lx": mx-lx, "pivot": pivot})
                
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    print_state("Base case: k == nl - 1")
                    return sorted([pivot, xs[mx+1], ys[my]])[:2]
                    if my < len(ys):
                        return sorted([pivot, xs[mx+1], ys[my]])[:2]
                    else:
                        print_state("EXTRA TRICKY: my >= len(ys)")
                        return [pivot, xs[mx+1]]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
                    
f = bulk_test_median()
from statistics import median
from collections import namedtuple

def bulk_test_median(num_random_tests=1000, size=range(100, 5000), elems=range(-5000, 5000), *cases, **named_cases):
    ind = "    "
    failed = []
    num_tests = 0
    s = Solution()
    MedianTestCase = namedtuple("MedianTestCase", ["xs", "ys", "expected"])
    def _random_test(sz):
        nx = randint(0, sz)
        xs = sorted([choice(elems) for _ in range(nx)])
        ys = sorted([choice(elems) for _ in range(sz-nx)])
        expected = median(xs + ys)
        return MedianTestCase(xs, ys, expected)
    def _test(s, tc, show_output=False, indent=ind):
        s.chatty(show_output, indent)
        found = s.findMedianSortedArrays(tc.xs, tc.ys)
        if found != tc.expected:
            s.chatty(True, "")
            s.define("Oh no!  Test failed:", expected=tc.expected, found=found)
        else:
            s.print("You passed, son")
        return found
    for name, c in named_cases.items():
        print(f"{name.upper()}:")
        _test(s, c, show_output=True, indent=2*ind)
        num_tests += 1
    for i, c in enumerate(cases):
        print(f"NUMBERED TESTCASE: ({i})")
        _test(s, c, show_output=True, indent=2*ind)
        num_tests += 1
    for _ in range(num_random_tests):
        tc = _random_test(choice(size))
        found = _test(s, tc)
        if found != tc.expected:
            failed.append(tc)
            print(f"RANDOM TEST FAILED:")
            _test(s, tc, show_output=True, indent=2*ind)
        num_tests += 1
    s.chatty(True, "")
    s.define("BULK TEST COMPLETE:", **{"tests run": num_tests, "tests failed": len(failed)})
    return failed
    
f = bulk_test_median()
from statistics import median
from collections import namedtuple

def bulk_test_median(num_random_tests=1000, size=range(100, 5000), elems=range(-5000, 5000), *cases, **named_cases):
    ind = "    "
    failed = []
    num_tests = 0
    s = Solution()
    MedianTestCase = namedtuple("MedianTestCase", ["xs", "ys", "expected"])
    def _random_test(sz):
        nx = randint(0, sz)
        xs = sorted([choice(elems) for _ in range(nx)])
        ys = sorted([choice(elems) for _ in range(sz-nx)])
        expected = median(xs + ys)
        return MedianTestCase(xs, ys, expected)
    def _test(s, tc, show_output=False, indent=ind):
        s.chatty(show_output, indent)
        found = s.findMedianSortedArrays(tc.xs, tc.ys)
        if found != tc.expected:
            s.chatty(True, "")
            s.define("Oh no!  Test failed:", expected=tc.expected, found=found)
        else:
            s.print("You passed, son")
        return found
    for name, c in named_cases.items():
        print(f"{name.upper()}:")
        _test(s, c, show_output=True, indent=2*ind)
    for i, c in enumerate(cases):
        print(f"NUMBERED TESTCASE: ({i})")
        _test(s, c, show_output=True, indent=2*ind)
    s.chatty(True, "")
    s.define("BEGINNING BULK TEST:", **{"random tests": num_random_tests})
    previous_update = 0
    for _ in range(num_random_tests):
        if num_tests / num_random_tests > previous_update + 10:
            print(f"{num_tests} run, {100*num_tests/num_random_tests}% complete...")
        tc = _random_test(choice(size))
        found = _test(s, tc)
        if found != tc.expected:
            failed.append(tc)
            print(f"RANDOM TEST FAILED:")
            _test(s, tc, show_output=True, indent=2*ind)
        num_tests += 1
    s.chatty(True, "")
    s.define("BULK TEST COMPLETE:", **{"tests run": num_tests, "tests failed": len(failed)})
    return failed
    
f = bulk_test_median()
from statistics import median
from collections import namedtuple

def bulk_test_median(num_random_tests=1000, size=range(100, 5000), elems=range(-5000, 5000), *cases, **named_cases):
    ind = "    "
    failed = []
    num_tests = 0
    s = Solution()
    MedianTestCase = namedtuple("MedianTestCase", ["xs", "ys", "expected"])
    def _random_test(sz):
        nx = randint(0, sz)
        xs = sorted([choice(elems) for _ in range(nx)])
        ys = sorted([choice(elems) for _ in range(sz-nx)])
        expected = median(xs + ys)
        return MedianTestCase(xs, ys, expected)
    def _test(s, tc, show_output=False, indent=ind):
        s.chatty(show_output, indent)
        found = s.findMedianSortedArrays(tc.xs, tc.ys)
        if found != tc.expected:
            s.chatty(True, "")
            s.define("Oh no!  Test failed:", expected=tc.expected, found=found)
        else:
            s.print("You passed, son")
        return found
    for name, c in named_cases.items():
        print(f"{name.upper()}:")
        _test(s, c, show_output=True, indent=2*ind)
    for i, c in enumerate(cases):
        print(f"NUMBERED TESTCASE: ({i})")
        _test(s, c, show_output=True, indent=2*ind)
    s.chatty(True, "")
    s.define("BEGINNING BULK TEST:", **{"random tests": num_random_tests})
    previous_update = 0
    for _ in range(num_random_tests):
        if num_tests / num_random_tests > previous_update + 10:
            previous_update = 100*num_tests/num_random_tests
            print(f"{num_tests} run, {previous_update}% complete...")
        tc = _random_test(choice(size))
        found = _test(s, tc)
        if found != tc.expected:
            failed.append(tc)
            print(f"RANDOM TEST FAILED:")
            _test(s, tc, show_output=True, indent=2*ind)
        num_tests += 1
    s.chatty(True, "")
    s.define("BULK TEST COMPLETE:", **{"tests run": num_tests, "tests failed": len(failed)})
    return failed
    
f = bulk_test_median()
from statistics import median
from collections import namedtuple

def bulk_test_median(num_random_tests=1000, size=range(100, 5000), elems=range(-5000, 5000), *cases, **named_cases):
    ind = "    "
    failed = []
    num_tests = 0
    s = Solution()
    MedianTestCase = namedtuple("MedianTestCase", ["xs", "ys", "expected"])
    def _random_test(sz):
        nx = randint(0, sz)
        xs = sorted([choice(elems) for _ in range(nx)])
        ys = sorted([choice(elems) for _ in range(sz-nx)])
        expected = median(xs + ys)
        return MedianTestCase(xs, ys, expected)
    def _test(s, tc, show_output=False, indent=ind):
        s.chatty(show_output, indent)
        found = s.findMedianSortedArrays(tc.xs, tc.ys)
        if found != tc.expected:
            s.chatty(True, "")
            s.define("Oh no!  Test failed:", expected=tc.expected, found=found)
        else:
            s.print("You passed, son")
        return found
    for name, c in named_cases.items():
        print(f"{name.upper()}:")
        _test(s, c, show_output=True, indent=2*ind)
    for i, c in enumerate(cases):
        print(f"NUMBERED TESTCASE: ({i})")
        _test(s, c, show_output=True, indent=2*ind)
    s.chatty(True, "")
    s.define("BEGINNING BULK TEST:", **{"random tests": num_random_tests})
    previous_update = 0
    for _ in range(num_random_tests):
        if 100*num_tests / num_random_tests > previous_update + 10:
            previous_update = 100*num_tests/num_random_tests
            print(f"{num_tests} run, {previous_update}% complete...")
        tc = _random_test(choice(size))
        found = _test(s, tc)
        if found != tc.expected:
            failed.append(tc)
            print(f"RANDOM TEST FAILED:")
            _test(s, tc, show_output=True, indent=2*ind)
        num_tests += 1
    s.chatty(True, "")
    s.define("BULK TEST COMPLETE:", **{"tests run": num_tests, "tests failed": len(failed)})
    return failed
    
f = bulk_test_median()
MedianTestCase = namedtuple("MedianTestCase", ["xs", "ys", "expected"])
cases = {"operator precedence": MedianTestCase([1, 3], [2], float(2)), "disjoint": MedianTestCase([1, 2], [3, 4]), "disjoint 2": MedianTestCase([*range(1, 4)], [*range(4, 11)])}
cases = {"operator precedence": MedianTestCase([1, 3], [2], float(2)), "disjoint": MedianTestCase([1, 2], [3, 4], float(2.5)), "disjoint 2": MedianTestCase([*range(1, 4)], [*range(4, 11)], float(5.5))}
f = bulk_test_median(**cases)
from bisect import bisect_right

class Solution:
    def chatty(self, isChatty, baseIndent=0):
        self._chatty = isChatty
        self._base_indent = baseIndent
    def print(self, msg=None, level=0, extra_defn_indent=0, **defns):
        if self._chatty:
            print(level*self.indent + self._base_indent + msg)
            for name, variable in defns.items():
                if len(name) >= self._max_varname_length:
                    self._max_varname_length = len(name) + 1
                print((level + extra_defn_indent)*self.indent + self._base_indent + f"{name} = ".rjust(self._max_varname_length) + str(variable))
    def define(self, header=None, level=1, **kwargs):
        if header is not None:
            self.print(header, level=level, extra_defn_indent=1, **kwargs)
        else:
            self.print(header, level=level, extra_defn_indent=0, **kwargs)
    def __init__(self):
        self._chatty = True
        self.indent = "    "
        self._max_varname_length = 15
        self._base_indent = ""
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x_o = sorted(nums1)
        y_o = sorted(nums2)
        pair = self.find_kth_pair(nums1, nums2, (len(nums1) + len(nums2) - 1)//2)
        self.print(f"Found median")
        if x_o != nums1 or y_o != nums2:
            self.print(f"=== MUTATION ALERT ===", 1)
        if (len(nums1) + len(nums2)) % 2 == 1:
            self.define("Case OOD:", level=1, median=float(pair[0]))
            return float(pair[0])
        else:
            self.define("Case EVEN:", level=1, median=sum(pair)/2.0)
            return sum(pair)/2.0

    def find_kth_pair(self, xs, ys, k):
        x_o = sorted(xs)
        y_o = sorted(ys)
        lx, ly, rx, ry = 0, 0, len(xs)-1, len(ys)-1
       
        def print_extended_state(header):
            self.define(header, level=0, **{"lx": lx, "ly": ly, "rx": rx, "ry": ry, "xs": xs, "ys": ys, "k": k, "x_o": x_o, "y_o": y_o})
        def print_state(header, **defns):
            self.define(header, level=0, **{"xs[lx:rx+1]": xs[lx:rx+1], "ys[ly:ry+1]": ys[ly:ry+1], "k": k, "expect": sorted(xs[lx:rx+1]+ys[ly:ry+1])[k]}, **defns)
        while True:
            nx, ny = rx - lx + 1, ry - ly + 1

            # WLOG, nx >= ny
            if nx < ny:
                xs, ys, lx, ly, rx, ry = ys, xs, ly, lx, ry, rx
                continue
            
            
            if ny <= 0:
                print_state("Base case: ny <= 0")
                return xs[lx+k:lx+k+2]
            elif nx + ny < 5:
                print_state("Base case: nx + ny < 5")
                return sorted(xs[lx:rx+1] + ys[ly:ry+1])[k:k+2]
            elif ny < 3:
                print_state("Base case: ny < 3")
                nums = list(xs[lx:rx+1])
                for y in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, y), y)
                return nums[k:k+2]
            elif k + 2 == nx + ny:
                print_state("Base case: k + 2 == nx + ny")
                return sorted(xs[rx-1:rx+1] + ys[ry-1:ry+1])[-2:]
            elif k == 0:
                print_state("Base case: k == 0")
                return sorted(xs[lx:lx+2] + ys[ly:ly+2])[:2]
            else:
                mx = (lx+rx)//2
                pivot = xs[mx]
                print_state("Iterating:", **{"mx - lx": mx-lx, "pivot": pivot})
                
                my = bisect_right(ys, pivot, ly, ry+1)
                nl = mx + my - lx - ly + 1
                if k == nl - 1:
                    print_state("Base case: k == nl - 1")
                    if my < len(ys):
                        return sorted([pivot, xs[mx+1], ys[my]])[:2]
                    else:
                        print_state("EXTRA TRICKY: my >= len(ys)")
                        return [pivot, xs[mx+1]]
                if k < nl:
                    rx, ry = mx, my-1
                else:
                    lx, ly = mx+1, my
                    k -= nl
                    
f = bulk_test_median(**cases)
f = bulk_test_median(num_random_tests=5000, **cases)
get_ipython().system('pwd')
get_ipython().run_line_magic('pwd', '')
