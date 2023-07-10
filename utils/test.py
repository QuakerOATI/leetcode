import sys
import random
from functools import wraps

def given(*strats):

    def select(n):
        def selector(*xs):
            return xs[n]
        return selector

    strat_generators = []
    nones = 0
    for s in strats:
        if s is None:
            strat_generators.append(select(nones))
            nones += 1
        elif callable(s):
            strat_generators.append(s)
        else:
            strat_generators.append(lambda *xs: s[0](*s[1:]))

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*map(lambda s: s(*args), strat_generators), **kwargs)
        return wrapper

    return decorator

def print_maybe(*args, quiet=False, **kwargs):
    if not quiet:
        print(*args, **kwargs)

def print_cases(cases, **values):
    for v, b in values.items():
        if b and v in cases:
            print(cases[v])

def test(fn):
    def wrapper(*args, quiet=False, reraise=False, **kwargs):
        status = "INTERRUPTED"
        print_cases({"loud": f"""
{"-"*50}
Running test {fn.__name__}:
    args: {args} 
    kwargs: {kwargs}
              """}, loud=not quiet)
        try:
            ret = fn(*args, **kwargs)
            print_cases({"loud": f"    --> {ret}"}, loud=not quiet)
            status = "PASSED"
        except AssertionError as e:
            print_cases({"loud": f"Assertion failed: {repr(e)}"}, loud=not quiet)
            status = "FAILED: ASSERTION"
            if reraise:
                raise e
        except Exception as e:
            exc_type, exc_value, tb = sys.exc_info()
            print_cases({"loud": f"""
Exception caught:
    type: {repr(exc_type)}
    value: {repr(exc_value)}
    traceback: {repr(tb)}
                """,
                "quiet": f"""
Exception: {repr(exc_value)}
    args: {args} 
    kwargs: {kwargs}
                """}, loud=not quiet, quiet=quiet)
            status = "FAILED: EXCEPTION"
            if reraise:
                raise e
        finally:
            print_cases({
                "loud": f"""

{status}
{"-"*50}
                """,
                "quiet": f"{status}: {args} {kwargs}"
            }, loud=not quiet, quiet=quiet)
    return wrapper

def test_assert(name, fn, *args, **kwargs):
    fail_reason = None
    try:
        ret = fn(*args, **kwargs)
        if not ret:
            fail_reason = f"Expected Truthy, got {ret}"
    except Exception as e:
        fail_reason = f"Exception: {e}"
    finally:
        if fail_reason is not None:
            print(f"{name.format(*args, **kwargs)}: {fail_reason}")

