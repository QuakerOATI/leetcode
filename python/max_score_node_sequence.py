from typing import List
from bisect import bisect_left


class Solution:

    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        adj = [[] for _ in range(len(scores))]
        for a, b in edges:
            adj[a].insert(bisect_left(adj[a], (scores[b], b)), (scores[b], b))
            adj[b].insert(bisect_left(adj[b], (scores[a], a)), (scores[a], a))

        best = -1
        for a, b in edges:
            try:
                best_outside = max(sc + sd for sc, c in adj[a][-3:]
                                   for sd, d in adj[b][-3:]
                                   if c != b and d != a and c != d)
                best = max(best, scores[a] + scores[b] + best_outside)
            except ValueError:
                continue
        return best
