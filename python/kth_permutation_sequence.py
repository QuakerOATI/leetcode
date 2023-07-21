from math import factorial


class Solution:

    def getPermutation(self, n: int, k: int) -> str:

        def helper(chars, k):
            m = len(chars)
            if m == 0:
                return ""
            elif m == 1:
                return chars[0]
            f = factorial(m - 1)
            first = chars.pop((k - 1) // f)
            return first + helper(chars, k % f)

        return helper([str(i) for i in range(1, n + 1)], k)
