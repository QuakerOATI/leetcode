"""
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

"""
from string import ascii_lowercase
from collections import Counter

class Solution:
    """
    86.71 %ile runtime
    31.55 %ile memory
    """
    def largestVariance(self, s):
        dp = Counter()
        S = Counter()
        M = 0
        for i, c1 in enumerate(s):
            S[c1] += 1
            for c2 in S:
                if c1 == c2:
                    continue
                if (c1, c2) not in dp:
                    dp[c1, c2] = (0, 1)
                    dp[c2, c1] = (S[c2] - 1, 0)
                else:
                    dp[c2, c1] = (dp[c2, c1][0] + dp[c2, c1][1] - 1, 0)
                    dp[c1, c2] = (max(0, dp[c1, c2][0] + 1), dp[c1, c2][1] if dp[c1, c2][0] >= 0 else 1)
                M = max(M, dp[c1, c2][0], dp[c2, c1][0])
        return M
