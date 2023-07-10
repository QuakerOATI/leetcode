from abc import ABC, abstractmethod


class WellOrdered(ABC):
    @abstractmethod
    def __lt__(self, other):
        ...

    @abstractmethod
    def __eq__(self, other):
        ...

    def __gt__(self, other):
        return not self == other and not self < other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other
