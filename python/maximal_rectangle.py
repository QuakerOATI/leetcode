from typing import List

class Solution:
    """
    This works, but exceeds allowed memory usage on (very) large testcases.
    It's also probably pretty slow.
    """
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        best = 0
        subs = {}
        H = len(matrix)
        L = len(matrix[0])

        for h in range(0, H):
            for w in range(0, L):
                subs[(h, w)] = set()
                found = False
                if h == 0 and w == 0:
                    subs[(h, w)] = {(i, j) for i in range(H) for j in range(L) if matrix[i][j] == "1"}
                    # determine if subs[(0, 0)] is empty
                    found = not subs[(h, w)].isdisjoint(subs[(h, w)])
                elif h == 0:
                    for i, j in subs[(h, w-1)]:
                        if j + w < L and (i, j+w) in subs[(0, 0)]:
                            subs[(h, w)].add((i, j))
                            found = True
                else:
                    for i, j in subs[(h-1, w)]:
                        if i + h < H and (i+h, j) in subs[(0, w)]:
                            subs[(h, w)].add((i, j))
                            found = True
                if found:
                    best = max(best, (h+1)*(w+1))
                else:
                    break

        return best
