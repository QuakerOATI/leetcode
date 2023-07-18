from collections import namedtuple


class TestGenerator:
    """Mixin to provide some convenience methods involving random testcases."""

    from random import randint, choice

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._test_elems = None
        self._test_sizes = None

    def withTestrange(self, elems=range(-1000, 1000), sizes=range(1000)):
        self._test_elems = elems
        self._test_sizes = sizes
        return self

    def get_random_sorted_list(self, elems=None, sizes=None, sz=None):
        elems = elems if elems is not None else self._test_elems
        sz = sz if sz is not None else self._test_sizes
        if not isinstance(sz, int):
            sz = self.choice(sz)
        nums = set()
        while len(nums) < sz:
            nums.add(self.choice(self._test_elems))
        return sorted(nums)


class Chatty:
    """Mixin to provide convenience methods for IO during testing and debugging."""

    from os import get_terminal_size

    SILENT = 0
    QUIET = 1
    TEST = 2
    DEBUG = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._get_terminal_dims()
        self._verbosity = self.TEST
        self._block_indents = []
        self._block_levels = []
        self._block_footers = []
        self._block_trim = []
        self._default_fence = "=" * self.COLUMNS
        self._default_trim = ["break", 10]

    def _getIndentLevel(self, idx=-1):
        return sum(self._block_indents[idx::-1])

    def _getBlockVerbosity(self, idx=-1):
        return sum(self._block_levels[idx::-1])

    def _talk(self, msg, verbosity, indentLevel, trimRight="break 10"):
        if self._verbosity < verbosity:
            return
        if trimRight is None:
            trimRight = self._block_trim[-1]
        trimRight = trimRight.lower().strip().split()
        if trimRight[0] == "default":
            trimRight = self._default_trim
        try:
            max_lines = int(trimRight)[1]
        except (IndexError, ValueError, TypeError):
            max_lines = -1
        trimRight = trimRight[0]
        indent = self._getRequestedIndent(indent)
        width = self.COLUMNS - indentLevel
        if len(msg) > width:
            if trimRight in ["break", "lb", "lines", "paragraph"]:
                lines = []
                while len(msg) > 0:
                    line, msg = msg[:width], msg[width:]
                    lines.append(indent + "| " + line)
                    if len(lines) > max_lines:
                        lines[-1] = lines[-1][:-3] + "..."
                        break
                print("\n".join(lines))
            elif trimRight in ["slice", "cut", "delete", "remove", "elide"]:
                print(indent + msg[:width])
        print(indent + msg)

    def _talkif(self, msg, verbosity, indentLevel, condition=None, trimRight=None):
        if condition is None or condition:
            self._talk(msg, verbosity, indentLevel, trimRight=trimRight)

    def _getRequestedIndent(self, indent):
        indent = indent.lower().strip()
        if indent is None:
            return ""
        elif indent == "block":
            return "".ljust(self._getIndentLevel())
        elif isinstance(indent, int):
            return "".ljust(indent)
        else:
            return indent

    def _print_fence(self, fence):
        if fence is None:
            return
        self.print(fence * self.width, trimRight="slice")

    @classmethod
    def _get_terminal_dims(cls):
        cls.COLUMNS, cls.LINES = cls.get_terminal_size()

    @property
    def width(self):
        return self.COLUMNS - self._getIndentLevel()

    def volume(self, level):
        self._verbosity = level
        return self

    def withTrim(self, trimRight):
        self._default_trim = trimRight.trim().lower().split()
        return self

    def printDebug(self, msg, condition=None, indent="block", trimRight=None):
        self._talkif(
            msg, self.DEBUG, indent, condition=condition, trimRight=trimRight
        )
        return self

    def printTest(self, msg, condition=None, indent="block", trimRight=None):
        self._talkif(
            msg, self.TEST, indent, condition=condition, trimRight=trimRight
        )
        return self

    def startBlock(self, level_inc=0, indent=0, fence="default", trimRight=None):
        if fence.lower().strip() == "default":
            fence = self._default_fence
        if trimRight is not None and trimRight.lower().strip() == "default":
            trimRight = self._default_trim
        self._block_trim = trimRight
        self._block_indents.append(indent)
        self._block_levels.append(level_inc)
        self._block_footers.append(fence)
        self._print_fence(fence)
        return self

    def endBlockScope(self, idx=-1):
        idx %= len(self._block_levels)
        while len(self._block_levels) - idx > 1:
            footer = self._block_footers.pop()
            self.print(footer, condition=footer is not None)
            self._block_levels.pop()
            self._block_indents.pop()
            self._block_trim.pop()
        return self

    def endBlock(self, idx=-1, footer=None):
        self.print(footer, condition=footer is not None)
        footer = self._block_footers.pop(idx)
        self.print(footer, condition=footer is not None)
        self._block_levels.pop(idx)
        self._block_indents.pop(idx)
        return self

    def withTitle(self, title, style="underline", colon=True):
        style = style.lower().lstrip().rstrip()
        if style == "underline":
            uline = len(title) * "-"
        elif style == "box":
            if colon:
                title += ":"
                colon = False
            title = f"| {title} |"
            uline = "+" + "-" * (len(title) - 2) + "+"
            self.print(uline)
        if colon:
            title += ":"
        return self.print(title).print(uline)

    def withFence(self, fence="="):
        self._default_fence = fence
        return self

    def print(self, msg, idx=-1, condition=None, trimRight="default"):
        self._talkif(
            msg,
            self._getBlockVerbosity(),
            self._getIndentLevel(),
            condition=condition,
            trimRight=trimRight,
        )
        return self

    def hline(self, char="-", length=30):
        return self.print(char * length)


class Timeable:
    """Mixin to provide basic benchmarking facilities."""

    from time import time as now

    class Timer:
        def __init__(self, owner):
            self._owner = owner
            self.start_times = []
            self.durations = []
            self.absolute = {}
            self.relative = {}

        def start(self, startName=None):
            self.start_times.append(t := self._owner.now())
            if startName is not None:
                self.absolute[startName] = t
            return self

        def stop(self, stopName=None, duration=None):
            if len(self.start_times) > 0:
                self.durations.append[
                    (t := self._owner.now()) - self.start_times.pop(0)
                ]
                if stopName is not None:
                    self.absolute[stopName] = t
                if duration is not None:
                    self.relative[duration] = self.durations[-1]
            return self

        def withMoment(self, name, relativeTo=None):
            if relativeTo is None:
                self.absolute[name] = self._owner.now()
            elif isinstance(relativeTo, int):
                self.relative[name] = self._owner.now() - self.start[relativeTo]
            else:
                self.relative[name] = self._owner.now() - self.relative[relativeTo]
            return self

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._timers = {}
        self._active_timer = None
        self.withTimer("root")

    @property
    def active_timer(self):
        return self._timers[self._active_timer]

    def withTimer(self, name, start=True, startName=None):
        self._timers.setdefault(name, self.Timer(self))
        self._active_timer = name
        if start:
            self.startTimer(startName)
        return self

    def startTimer(self, startName=None):
        self.active_timer.start(startName)
        return self

    def stopTimer(self, stopName=None, duration=None):
        self.active_timer.stop(stopName=stopName, duration=duration)
        return self

    def withMoment(self, name, relativeTo=None):
        self.active_timer.withMoment(name, relativeTo=relativeTo)
        return self


class Checkable:
    """Mixin to provide facilities for automatic answer-checking"""

    from .timeout import signal_timer

    class CheckException(Exception):
        pass

    results = {}
    events = {}
    cases = {}
    checkers = {}

    TestCase = namedtuple("TestCase", ["args", "kwargs", "expected"], defaults=[[], {}, None])
    TestResult = namedtuple(
        "TestResult",
        ["name", "testcase", "returned", "status", "exception"],
        defaults=[None, None, None],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def _insert_expectations(cls, testcase, event_name):
        expectations = {
            item[0]: item[1](*testcase.args, **testcase.kwargs)
            for item in cls.checkers.get(event_name, {}).items()
        }
        if isinstance(testcase.expected, dict):
            expectations = testcase.expected | expectations
        else:
            expectations |= {"GIVEN": testcase.expected}
        return cls.TestCase(**testcase, expected=expectations)

    @classmethod
    def add_checker(cls, event_name, check_func, check_name=None):
        if check_name is None:
            check_name = check_func.__name__
        cls.checkers.setdefault(event_name, {})
        cls.checkers[event_name][check_name] = check_func

    @classmethod
    def add_event(cls, event_name, func):
        cls.events.setdefault(event_name, [])
        cls.events[event_name].append(func)

    @classmethod
    def add_testcases(cls, event_name, *testcases):
        cls.cases.setdefault(event_name, [])
        cls.cases[event_name].extend(testcases)

    @classmethod
    def check_testcase(cls, event_name, testcase, use_checkers=False, reuse=True):
        cls.results.setdefault(event_name, [])
        if use_checkers:
            try:
                testcase = cls._insert_expectations(event_name, testcase)
            except Exception as e:
                raise cls.CheckException(
                    f"Exception caught while generating expectations for event {event_name}: {e}"
                )
        try:
            if reuse:
                cls.cases.setdefault(event_name, [])
                cls.cases[event_name].append(testcase)
            ret = cls.events[event_name](*testcase.args, **testcase.kwargs)
            status = None
            if testcase.expected is not None:
                status = ret == expected
            return cls.TestResult(
                event_name, testcase=case, returned=ret, status=status
            )
        except Exception as e:
            return cls.TestResult(event_name, testcase=testcase, status=False, exception=e)

    @classmethod
    def check_all_testcases(cls, event_name, use_checkers=False):
        try:
            for c in cls.cases[event_name]:
                cls.check_testcase(event_name, c, use_checkers=use_checkers, reuse=False)
        except KeyError:
            raise cls.CheckException(
                f"Lookup error when checking tests for event {event_name}"
            )


class Testable(TestGenerator, Chatty, Timeable, Checkable):
    def __init__(self):
        super().__init__()
        self._test_elems = range(-1000, 1000)
        self._test_sizes = range(1000)
        self._expected, self._result = None, None

    def _print_expectations(self, expected):
        self.startBlock(indent=4, fence=None).withTitle("Expected")
        if not isinstance(expected, dict):
            expected = {"GIVEN": expected}
        for name, predicted in expected.items():
            self.startBlock(indent=2, fence=None).print(
                f"{name.upper()}:        {predicted}"
            )
        self.endBlock()

    def _print_testresult(self, result: Checkable.TestResult):
        self.endBlockScope(idx=0).startBlock().withTitle(f"{result.name} results")
        self.startBlock(indent=4, fence=None).withTitle("Status").print(
            result.status
        ).endBlock()
        self._print_expectations(result.testcase.expected)
        self.startBlock(indent=4, fence=None).withTitle("Returned").print(
            result.returned
        ).endBlock()
        self.endBlockScope()

    def generate_testcase(self):
        return NotImplemented

    def test(self):
        self.generate_testcase()
        self.run_testcase()
        self._print_testresult()
