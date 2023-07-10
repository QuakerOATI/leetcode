from typing import List, NamedTuple
from random import choice, randint, choices
from time import time as now
from types import SimpleNamespace
from math import log2


class Solution:
    def __init__(self):
        self._testcases = {True: [], False: []}
        self._verbosity = 0

    def verbose(self, verbosity=3):
        self._verbosity = verbosity
        return self

    def silent(self):
        self._verbosity = 0
        return self

    @property
    def failed(self):
        return self._testcases[False]

    @property
    def succeeded(self):
        return self._testcases[True]

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        N = len(nums)
        l, r = 0, N - 1
        pivot = 0

        while nums[r] < nums[l]:
            if r == l + 1:
                pivot = N - r
                break
            m = self.halve(r + l)

            for x in l, r, m:
                if nums[x] == target:
                    return x
            if nums[r] < nums[m]:
                l = m
            else:
                r = self.halve(r + l, True)
        lo, ro = (self.get_offset_idx(N, i, pivot) for i in (0, N - 1))

        while nums[lo] < target < nums[ro]:
            l, r = (self.get_true_idx(N, i, pivot) for i in (lo, ro))
            if r == l + 1:
                return -1
            m = self.halve(l + r)
            mo = self.get_offset_idx(N, m, pivot)
            if nums[mo] == target:
                return mo
            elif nums[mo] < target:
                lo = mo
            else:
                ro = self.get_offset_idx(N, self.halve(r + l, True), pivot)
        if target == nums[lo]:
            return lo
        elif target == nums[ro]:
            return ro
        return -1

    def get_offset_idx(self, arrlen, idx, pivot):
        return (idx - pivot) % arrlen

    def get_true_idx(self, arrlen, idx, pivot):
        return (idx + pivot) % arrlen

    def halve(self, x, round_up=False):
        return x // 2 + int(x % 2 == 1 and round_up)

    def test(self, num_trials=100, **kwargs):
        for _ in range(num_trials):
            self.silent().run_random_testcase(**kwargs)
        print(f"Num successes: {len(self.succeeded)}")
        print(f"Num failures: {len(self.failed)}")

    def run_random_testcase(self, **kwargs):
        case = self.TestCase.random(**kwargs)
        try:
            case.returned = self.search(case.nums, case.target)
            case.exception = None
        except AttributeError:
            raise self.TestCase.TestCaseError("Testcase not properly initialized")
        except Exception as e:
            case.exception = e
            case.returned = None
        finally:
            case.record_time("runtime")
            case.close()
            self._testcases[case.success].append(case)
            if self._verbosity > 0:
                case.talk(self._verbosity)

    class TestCase(SimpleNamespace):
        class TestCaseError(Exception):
            pass

        def __init__(self):
            for name in "time", "sizes":
                super().__setattr__(name, SimpleNamespace())
            self._start = now()

        def record_time(self, name):
            self.time.__setattr__(name, now() - self._start)

        def record_time_from(self, name_new, name_old):
            try:
                self.time.name_new = now() - self.time.name_old
            except AttributeError:
                raise self.TestCaseError(f"Timestamp {name_old} not found")

        def record_and_reset(self, name):
            self.record_time(name)
            self.reset_timer()

        def reset_timer(self):
            self._start = now()

        def _set_N(self, N):
            lgN = log2(N)
            self.sizes.N = []
            self.sizes.logN = []
            for p in range(4):
                self.sizes.N.append(N**p)
                self.sizes.logN.append(lgN**p)

        def set_nums(self, nums, pivot):
            self.pivot = pivot
            nums = sorted(nums)
            self.sizes.min_elem, self.sizes.max_elem = nums[0], nums[-1]
            self.nums = [*nums[self.pivot :], *nums[: self.pivot]]
            self._set_N(len(nums))

        def set_target(self, target):
            self.target = target

        def close(self):
            try:
                self.success = self.returned == self.expected
            except AttributeError:
                raise self.TestCaseError("Could not close testcase")

        @property
        def expected(self):
            try:
                return self.nums.index(self.target)
            except ValueError:
                return -1

        def _show_attribute(self, getter, *names):
            ret = getter(self)
            show = " " * 4 + "::".join(names).rjust(20)
            print(show)
            print(" " * 28 + f"--> {ret}")

        def _show_size_info(self):
            self._show_attribute(lambda s: s.sizes.N[1], "sizes::N")
            self._show_attribute(lambda s: s.sizes.N[2], "sizes::N**2")
            self._show_attribute(lambda s: s.sizes.logN[1], "sizes::logN")
            self._show_attribute(
                lambda s: s.sizes.N[1] * s.sizes.logN[1], "sizes::N*logN"
            )

        def _show_success_info(self):
            if self.success:
                print("Success!")
            else:
                print("TESTCASE FAILED")
                self._show_attribute(lambda s: s.expected, "expected")
                self._show_attribute(lambda s: s.returned, "returned")

        def _show_time_info(self):
            self._show_attribute(lambda s: s.time.runtime, "runtime")

        def talk(self, verbosity=1):
            if verbosity < 1:
                return
            try:
                print("=" * 50)
                self._show_success_info()
                if verbosity > 1:
                    self._show_time_info()
                if verbosity > 2:
                    self._show_size_info()
                print("=" * 50)
            except AttributeError:
                pass

        @classmethod
        def random(cls, arrlen=range(1, 100), elems=range(-1000, 1000)):
            case = cls()
            N = choice(arrlen)
            nums = set()
            while len(nums) < N:
                nums.add(choice(elems))
            case.set_nums(nums, randint(0, N - 1))
            case.set_target(choice(range(case.sizes.min_elem, case.sizes.max_elem + 1)))
            case.record_and_reset("testcase_generation")
            return case
