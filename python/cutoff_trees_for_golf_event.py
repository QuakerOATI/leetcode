"""From a mock-screening test for Amazon"""

from typing import List
from collections import namedtuple, deque
from queue import PriorityQueue
from itertools import product

class PointMatrix:
    Point = namedtuple("Point", ["x", "y"])
    def __init__(self, mat):
        self._mat = mat
        self.m, self.n = len(mat), len(mat[0])
    def __getitem__(self, p):
        return self._mat[p.x][p.y]
    def __setitem__(self, p, val):
        self._mat[p.x][p.y] = val
    def neighbors(self, p):
        x, y = p
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            q = self.Point(x+dx, y+dy)
            if 0 <= q.x < self.m and 0 <= q.y < self.n:
                yield q
    def find(self, pred):
        if not callable(pred):
            pred = lambda x: x == pred
        for x, y in product(range(self.m), range(self.n)):
            if pred(self[p := self.Point(x, y)]):
                yield p
    def __iter__(self):
        return (self.Point(x, y) for x in range(self.m) for y in range(self.n))
    def __repr__(self):
        return repr(self._mat)

class Solution:
    class Forest(PointMatrix):
        def __init__(self, mat):
            super().__init__(mat)
            self._dist = PointMatrix(
                [[PointMatrix([[None for _ in range(self.n)] for _ in range(self.m)]) for _ in range(self.n)] for _ in range(self.m)]
            )
            for x in range(self.m):
                for y in range(self.n):
                    p = self.Point(x, y)
                    self._dist[p][p] = 0
        def distance(self, p1, p2):
            """Cached BFS"""
            if (d := self._dist[p1][p2]) is not None:
                return d
            elif (d := self._dist[p2][p1]) is not None:
                self._dist[p1][p2] = d
                return d
            queue = deque([p1])
            seen = set([p1])
            numProcessed = 0
            while self._dist[p1][p2] is None and len(queue) > 0:
                if numProcessed > self.m*self.n:
                    print(f"queue: {queue}")
                    print(f"seen: {seen}")
                    raise OverflowError("Too many dicks on the dancefloor")
                d = self._dist[curr := queue.popleft()][p1]
                # if curr in seen:
                #     continue
                # seen.add(curr)
                if (dc := self._dist[curr][p2]) is not None:
                    if dc == -1:
                        return -1
                    return d + dc
                for n in self.neighbors(curr):
                    # Make sure we cache these before short-circuiting
                    if self._dist[p1][n] is None:
                        self._dist[p1][n] = d + 1
                        self._dist[n][p1] = d + 1
                    if n not in seen:
                        queue.append(n)
                        seen.add(n)
                numProcessed += 1
            if self._dist[p1][p2] is None:
                self._dist[p1][p2] = -1
                self._dist[p2][p1] = -1
            return self._dist[p1][p2]
        def neighbors(self, p):
            yield from filter(lambda q: self[q] > 0, super().neighbors(p))

    def __init__(self):
        self.forest = None

    def cutOffTree(self, forest: List[List[int]]) -> int:
        self.forest = self.Forest(forest)
        heights = [(f, self.Forest.Point(x, y)) for x in range(self.forest.m) for y in range(self.forest.n) if (f := forest[x][y]) > 1]
        heights.sort(key=lambda pair: pair[0], reverse=True)
        tot = 0
        curr = self.Forest.Point(0, 0)
        while len(heights) > 0:
            t = heights.pop()
            tot += (d := self.forest.distance(curr, t[1]))
            if d < 0:
                return -1
            curr = t[1]
        return tot
