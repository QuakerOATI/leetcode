import os


def write_transient(msg):
    print(msg, end="\r" + "".ljust(len(msg)) + "\r")


class TerminalWriter:
    def __init__(self):
        self.WIDTH, self.HEIGHT = os.get_terminal_size()


class StatusWriter(TerminalWriter):
    def __init__(self, initial_status):
        super().__init__()
        self._status = initial_status
        self._listener = self._get_listener(initial_status)
        self._listener.send(None)

    def print(self, msg):
        self._clear()
        print(msg)
        self._listener.send(self._status)

    def update(self, status):
        self._clear()
        self._status = status
        self._listener.send(self._status)

    def _clear(self):
        print("\r" + "".ljust(self.WIDTH), end="\r")

    def _get_listener(self, initial_status):
        print(initial_status, end="\r")
        while True:
            status = yield
            self._clear()
            print(status, end="\r")
