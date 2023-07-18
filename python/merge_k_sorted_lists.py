import sys
from abc import ABC, abstractmethod
from typing import Optional, List, Any, NamedTuple
from collections import namedtuple
from contextlib import contextmanager
from multiprocessing import Queue

"""
imap_unordered
starmap / starmap_async
AsyncResult.wait(timeout)
    need to check status with result.ready()
Pool.terminate()
    abort all child processes
context manager:
    calls Pool.terminate() in __exit__
Pool(initializer=..., initargs=...)
"""


class TestRunner(Process):
    def __init__(self):
        class NullWriter(object):
            def print(self, msg):
                print(msg)

        self._writer = NullWriter()


class BasicSolution(ABC):
    from timeit import default_timer as now
    from datetime import datetime

    TestLog = namedtuple("TestLog", ["passed", "failed", "throws"])

    class TestCase(NamedTuple):
        expected: Any

    def __init__(self):
        self._chattiness = 1
        self._indent = 0
        self._defn_align = 15
        self._kw_translate = {"_": " "}
        self._shiftwidth = 4
        self.tests = self.TestLog()
        self.TestResult = namedtuple(
            "TestResult",
            list(self.TestCase._fields)
            + ["timestamp", "returned", "runtime", "exception"],
            defaults=[None],
        )

    def _translate_name(self, name):
        for c1, c2 in self._kw_translate.items():
            name = name.replace(c1, c2)
        return name

    def _print_indented(self, msg):
        print("".ljust(self._indent * self._shiftwidth) + msg)

    def timestamp(self):
        return self.datetime.now().isoformat()

    @contextmanager
    def section(self, header):
        if header is not None:
            self.print(header)
            self._indent += 1
        try:
            yield self
        finally:
            if header is not None:
                self._indent -= 1

    @contextmanager
    def relative_indent(self, ilevel=1):
        self._indent += ilevel
        try:
            yield self
        finally:
            self._indent -= ilevel

    @contextmanager
    def absolute_indent(self, ilevel=0):
        old = self._indent
        self._indent = ilevel
        try:
            yield self
        finally:
            self._indent = old

    def aside(self, chattiness, msg, msg_chattiness=0, ilevel=0, **kwargs):
        with self.absolute_indent(ilevel):
            old = self._chattiness
            self._chattiness = chattiness
            self.print(msg, msg_chattiness, **kwargs)
            self._chattiness = old

    def print(self, msg, chattiness=0, **kwargs):
        if self._chattiness >= chattiness:
            self._print_indented(msg)
            if len(kwargs) > 0:
                with self.relative_indent(1):
                    for k, v in kwargs.items():
                        name = self._translate_name(str(k))
                        self._defn_align = max(self._defn_align, len(name) + 2)
                        self._print_indented(
                            f"{name} = ".rjust(self._defn_align) + str(v)
                        )

    @abstractmethod
    def solve_testase(self, tc):
        ...

    def _run_testcase(self, reraise):
        tc = yield
        start = self.now()
        try:
            ret = self.solve_testase(tc, reraise=reraise)
            result = self.TestResult(
                **tc,
                timestamp=self.timestamp(),
                returned=ret,
                runtime=self.now() - start,
                exception=None,
            )
        except Exception as e:
            result = self.TestResult(
                **tc, timestamp=self.timestamp(), returned=None, exception=e
            )
            if reraise:
                raise
        finally:
            return result

    def run_testcase(self, tc, reraise=False):
        self._run_testcase.send(tc)

    @contextmanager
    def TestRunner(self, stop_on_exception=False):
        try:
            test = None
            yield self
            while True:
                test = yield
                ret = self._run_testcase(test, reraise=stop_on_exception)
                if ret.exception is not None:
                    self.tests.throws.append(ret)
                elif ret.returned is not None and ret.returned == test.expected:
                    self.tests.passed.append(ret)
                else:
                    self.tests.failed.append(ret)
        except Exception as e:
            if test is not None:
                self.tests.throws.append(
                    self.TestResult(
                        **test, runtime=self.now() - start, returned=None, exception=e
                    )
                )

    def run_testcase(self, tc, comment=None):
        with self.section(comment) as sect:
            sect.print(head1=tc.lists[0], head2=tc.lists2)


def linked_list(arr):
    head = None
    for x in list(arr)[-1::-1]:
        head = ListNode(x, next=head)
    return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        x, y = self, other
        while x is not None:
            if y is None or x.val != y.val:
                return False
            x, y = x.next, y.next
        if y is not None:
            return False
        return True


class Solution(BasicSolution):
    from random import choice

    TestCase = namedtuple("TestCase", ["lists", "merged"])

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ...

    def generate_testcase(self, num_lists, sizes=range(1000), elems=range(-1000, 1000)):
        lists = []
        allnums = []
        for _ in num_lists:
            sz = self.choice(sizes)
            arr = sorted([self.choice(elems) for _ in range(sz)])
            lists.append(linked_list(arr))
            allnums.extend(arr)
        allnums.sort()
        return self.TestCase(lists, allnums)

    def run_testcase(self, tc, comment=None):
        with self.section(comment) as sect:
            sect.print(head1=tc.lists[0], head2=tc.lists2)
