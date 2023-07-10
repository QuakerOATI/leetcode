class Solution:
    """
    Input:
        PAYPALISHIRING
    Output:
        P   A   H   N
        A P L S I I G
        Y   I   R
        --> PAHNAPLSIIGYIR

        A      G      M
        B    F H    L N
        C  E   I  K   O
        D      J      P

        N := 2*(r-1)

        (0::N)
        (1::N) and (N-1::N)
        (2::N) and (N-2::N)
    -------------------------
    0, 4, 8, 12, ...
    1, 3, 5, 7, ...
    2, 6, 10, 14, ...
    """

    def convert(self, s: str, numRows: int) -> str:
        return self._convert(s)

    @staticmethod
    def _convert(s: str, numRows: int) -> str:
        # cycle = 2*(n-1)
        # if len(s) < 4:
        #     return s
        # return s[::4] + s[1::2] + s[2::4]
        if len(s) < numRows + 1 or numRows < 2:
            return s
        ret = ""
        N = 2 * (numRows - 1)
        for row in range(numRows):
            ret += "".join(
                [s[i] for i in range(len(s)) if i % N == row or i % N == N - row]
            )
        return ret
