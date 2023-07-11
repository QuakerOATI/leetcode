from contextlib import contextmanager
from multiprocessing import Process
import threading
import _thread
import signal


def _basic_timeout(func, args, kwargs, time):
    """From https://stackoverflow.com/questions/366682/how-to-limit-execution-time-of-a-function-call"""
    p = Process(target=func, args=args, kwargs=kwargs)
    p.start()
    p.join(time)
    if p.is_alive():
        p.terminate()
        return False
    return True


def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    """This function will spwan a thread and run the given function using the args, kwargs and
    return the given default value if the timeout_duration is exceeded
    """
    import threading

    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = default

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except:
                self.result = default

    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return it.result
    else:
        return it.result


@contextmanager
def time_limit(seconds):
    """Context manager to limit execution time.

    From https://stackoverflow.com/questions/366682/how-to-limit-execution-time-of-a-function-call
    """
    timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
    timer.start()
    try:
        yield
    except KeyboardInterrupt:
        pass
    finally:
        # if the action ends in specified time, timer is canceled
        timer.cancel()


@contextmanager
def signal_timer(seconds):
    """Context manager to limit execution time using signals.

    From https://stackoverflow.com/questions/366682/how-to-limit-execution-time-of-a-function-call
    """

    def signal_handler(signum, frame):
        raise TimeoutError

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
