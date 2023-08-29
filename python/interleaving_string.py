from collections import deque


class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Originally TLE on both memoized and DP approaches
        The key for this DP solution is to prevent redundancy in the entries of dp[]
        91.02 %ile runtime
        89.28 %ile memory
        """
        if len(s3) != len(s1) + len(s2):
            return False

        dp = deque()
        dp.append((0, 0))
        seen = set()

        for i in range(len(s3)):
            seen.clear()
            if len(dp) == 0:
                return False
            while len(dp) > 0 and sum(dp[-1]) == i:
                j1, j2 = dp.pop()
                if j1 < len(s1) and s1[j1] == s3[i] and (j1 + 1,
                                                         j2) not in seen:
                    dp.appendleft((j1 + 1, j2))
                    seen.add((j1 + 1, j2))
                if j2 < len(s2) and s2[j2] == s3[i] and (j1,
                                                         j2 + 1) not in seen:
                    dp.appendleft((j1, j2 + 1))
                    seen.add((j1, j2 + 1))

        return len(dp) > 0
