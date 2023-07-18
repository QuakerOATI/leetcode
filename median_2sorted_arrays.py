from typing import List
from bisect import bisect_right, bisect_left
from utils.testable import Testable


class Solution(Testable):
    SHORT_CIRCUIT_LENGTH = 3

    def __init__(self):
        super().__init__()
        self.add_event("find_kth", self.find_kth)

    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        """
        needs to be O(log(len(n1) + len(n2)))
        """
        ...

    def median(self, sorted_arr):
        n = len(sorted_arr)
        if n == 0:
            return None
        if n % 2 == 0:
            return (sorted_arr[n / 2] + sorted_arr[1 + n / 2]) / 2
        else:
            return sorted_arr[(n + 1) / 2]

    def find_kth(self, xs, ys, k):
        """
        assumptions:
            - xs and ys are sorted
            - ys[k] <= xs[-1] for all k
            - xs[k] >= ys[0] for all k
        Approach:
            - split both xy and ys at the median of the larger set
            [*xs, *ys] --> [*us | M | *vs]
        """
        if len(xs) + len(ys) <= 2:
            return sorted([*xs, *ys])[k]

        lx, rx = 0, len(xs) - 1
        ly, ry = 0, len(ys) - 1

        while True:
            # WLOG, rx - lx >= ry - ly
            if rx - lx < ry - ly:
                # self._talkif("Switching xs and ys", self.DEBUG)
                xs, ys = ys, xs
                rx, ry, lx, ly = ry, rx, ly, lx
            # Base cases
            if ry < ly:
                # This one needs to be checked first
                # This was a major pain point :/
                return xs[lx + k]
            elif rx == lx:
                # self._talkif(f"Base case: rx == lx == {rx}", self.DEBUG)
                if k > 0:
                    return max(xs[rx], ys[ry])
                else:
                    return min(xs[rx], ys[ry])
            elif ry == ly:
                # Note that the right-hand endpoint is *not* inclusive for bisect_*
                i = bisect_right(xs, ys[ly], lx, rx+1)
                if i - lx > k:
                    return xs[lx + k]
                elif i - lx == k:
                    return ys[ly]
                else:
                    return xs[lx + k - 1]

            split_x = (rx + lx) // 2  # "left-midpoint"
            # Edge case: repeated values in xs
            # It actually doesn't matter if we hit a long streak of repeating values
            # split_x = bisect_right(xs, xs[split_x], lx, ry)
            split_y = bisect_right(ys, xs[split_x], ly, ry+1) - 1  # O(log(Y))
            sz_left = split_x + split_y - lx - ly + 2

            if k >= sz_left:
                # These checks are not necessary...in fact they helped mask the true bug
                # lx = min(len(xs)-1, split_x + 1)
                # ly = min(len(ys)-1, split_y + 1)
                lx = split_x + 1
                ly = split_y + 1
                k -= sz_left
            else:
                rx = split_x
                ry = split_y

    def find_kth_pair(self, xs, ys, k):
        """Slightly modified from above to find the *pair* of elements at indices k, k+1
        """

        lx, rx = 0, len(xs) - 1
        ly, ry = 0, len(ys) - 1

        while True:

            # WLOG, rx - lx >= ry - ly
            if rx - lx < ry - ly:
                xs, ys = ys, xs
                rx, ry, lx, ly = ry, rx, ly, lx

            if rx + ry - lx - ly < k:
                return [max(xs[rx], ys[ry]), min(xs[rx+1], ys[ry+1])]

            # Base case
            if ry - ly + 1 < self.SHORT_CIRCUIT_LENGTH:
                nums = list(xs[lx:rx+1])
                for elem in ys[ly:ry+1]:
                    nums.insert(bisect_right(nums, elem), elem)
                return nums[k:k + 2]

            elif rx + ry - lx - ly + 2 < 2*self.SHORT_CIRCUIT_LENGTH:          # 5 seems like a good number
                return sorted([*xs[lx:rx+1], *ys[ly:ry+1]])[k:k+2]

            split_x = (rx + lx) // 2  # "left-midpoint"
            split_y = bisect_right(ys, xs[split_x], ly, ry+1) - 1  # O(log(Y))
            sz_left = split_x + split_y - lx - ly + 2

            if k >= sz_left:
                lx = split_x + 1
                ly = split_y + 1
                k -= sz_left
            else:
                rx = split_x
                ry = split_y
        

    def generate_testcase(self):
        xs, ys = [self.get_random_sorted_list() for _ in range(2)]
        k = self.choice(range(len(xs) + len(ys) - 1))
        expected = sorted([*xs, *ys])[k]
        return self.TestCase(args=[self, xs, ys, k], kwargs={}, expected=expected)
