"""From a mock-screening test for Amazon"""

from typing import List, NamedTuple
from collections import deque
from itertools import product


class Cell(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return self.__class__(-self.x, -self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def flipped(self):
        return self.__class__(self.y, self.x)


class CellMatrix:
    """Convenience class for traversing the graph represented by the cells of a 2x2 matrix."""

    NORTH = Cell(-1, 0)
    SOUTH = Cell(1, 0)
    EAST = Cell(0, 1)
    WEST = Cell(0, -1)

    def __init__(self, mat):
        self._mat = mat
        # No ragged matrices
        self.m, self.n = len(mat), len(mat[0])

    def __getitem__(self, p):
        return self._mat[p.x][p.y]

    def __setitem__(self, p, val):
        self._mat[p.x][p.y] = val

    def __contains__(self, p):
        return 0 <= p.x < self.m and 0 <= p.y < self.n

    def neighbors(self, p):
        for direction in [self.NORTH, self.SOUTH, self.EAST, self.WEST]:
            q = p + direction
            if q in self and self[q] > 0:
                yield q

    def find(self, pred):
        if not callable(pred):

            def pred(x):
                return x == pred

        yield from filter(lambda p: pred(p), iter(self))

    def __iter__(self):
        return (Cell(x, y) for x in range(self.m) for y in range(self.n))

    def __repr__(self):
        return repr(self._mat)


class SymmetrizedMatrix:

    def __init__(self, mat):
        self._mat = mat

    def __getitem__(self, tup):
        ret = self._mat[tup[0]][tup[1]]
        return ret if ret is not None else self._mat[tup[1]][tup[0]]

    def __setitem__(self, tup, value):
        self._mat[tup[0]][tup[1]] = value
        self._mat[tup[1]][tup[0]] = value

    def __repr__(self):
        return repr(self._mat)


def allSourceBFS(inst):
    print("Calling allSourceBFS")
    distances = SymmetrizedMatrix(
        CellMatrix([[
            CellMatrix([[None for _ in range(inst.n)] for _ in range(inst.m)])
            for _ in range(inst.n)
        ] for _ in range(inst.m)]))
    queue = deque()
    seen = set()
    # numPoints = 0
    for x, y in [(x, y) for x in range(inst.m) for y in range(inst.n)]:
        p = Cell(x, y)
        # numPoints += 1
        # if numPoints > inst.m * inst.n:
        #     print(f"Something has gone very, very wrong here")
        distances[p, p] = 0
        queue.clear()
        seen.clear()
        queue.append(p)
        seen.add((*p, ))
        numProcessed = 0
        print("About to iterate...")
        while len(queue) > 0:
            # print(queue.popleft())
            # print(f"Entering loop iteration {numProcessed}...")
            if numProcessed > inst.m * inst.n:
                print(
                    f"WARNING: BFS queue is abnormally large for search beginning with coordinate {p}"
                )
                print(f"Queue state: [...{list(queue)[-10:]}]")
                raise OverflowError("BFS overflowed, dawg")
            numProcessed += 1
            q = queue.popleft()
            print(f"After popping: {len(queue)}")
            d = distances[p, q]
            for n in inst.neighbors(q):
                # if (*n, ) not in seen and q in seen:
                #     seen.add((*n, ))
                #     queue.append(n)
                if q in seen:
                    if (*n, ) not in seen:
                        queue.append(n)
                    seen.add((*n, ))
                dn = distances[p, n]
                if dn is None:
                    distances[p, n] = d + 1
                else:
                    distances[p, n] = min(d + 1, dn)
            print(f"After appending: {len(queue)}")
    return distances


class BFSCellMatrix(CellMatrix):

    def __init__(self, mat):
        super().__init__(mat)
        self._dist = allSourceBFS(self)

    @staticmethod
    def distance(self, p, q):
        d = self._dist[p, q]
        return d if d is not None else -1


class Solution:

    class Forest(BFSCellMatrix):

        def neighbors(self, p):
            yield from filter(lambda q: self[q] > 0, super().neighbors(p))

    def __init__(self):
        self.forest = None

    def cutOffTree(self, forest: List[List[int]]) -> int:
        self.forest = self.Forest(forest)
        heights = [(h, p) for p in self.forest if (h := self.forest[p]) > 1]
        heights.sort(key=lambda pair: pair[0], reverse=True)
        tot = 0
        curr = Cell(0, 0)
        while len(heights) > 0:
            t = heights.pop()
            print(f"Traveling to tree {t[1]} at height {t[0]}...")
            tot += (d := self.forest.distance(curr, t[1]))
            print(f"    Distance traveled: {d}")
            print(f"    Total: {tot}")
            if d < 0:
                print("Abort!")
                return -1
            curr = t[1]
        return tot
