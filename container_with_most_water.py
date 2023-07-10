from typing import List


class Solution:
    """Accepted

    Terrible runtime though, for reasons I should explore
    ----------------------------S1: sort
    [(j_k, H_k) : H_k <= H_{k+1} . k]

    ----------------------S2: remove minima
    ignore H_0 if:
        i_0 is not min(i_k) or max(i_k)
    else:
        found.add(H_0*<range>)
    then:
        found.add(ans for H[1:])

    ----------------------S2: reduce heights
    ignore H_0 if:
        max([i_0, N-i_0], key=abs)*H_0 <= ...
    """

    def maxArea(sef, height: List[int]) -> int:
        hs = sorted(enumerate(height), reverse=True, key=lambda t: t[1])
        visited = set()
        l, r = 0, len(hs) - 1
        best = 0
        while len(hs) > 1:
            hmin = hs.pop()
            visited.add(hmin[0])
            if hmin[0] == l or hmin[0] == r:
                best = max(hmin[1] * (r - l), best)
                while l in visited:
                    l += 1
                while r in visited:
                    r -= 1
        return best
