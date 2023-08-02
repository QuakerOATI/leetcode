"""
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

"""
from itertools import combinations

class Solution:
    def largestVariance(self, s):
        """TLE"""
        S = set(s)
        if len(S) < 2:
            return 0
        M = 0
        for chars in combinations(S, 2):
            count = [{c1: [[0, 0], [0, 0]] for c1 in chars}]
            # ct[x][k][l] := maximal (#x - #y) for substrings ending at pos which contains at least k xs and l ys
            for c in s:
                if c not in chars:
                    continue
                prev = count[-1]
                ct = {c1: [[0, 0], [0, 0]] for c1 in chars}
                for x, y in zip(chars, reversed(chars)):
                    if x == c:
                        ct[x][0] = count[-1]
                        ct[x][y] = count[-1][x][y] + 1
                    else:
                        ct[x][x] = max(count[-1][x][y] - 1, 0)
                        ct[x][y] = count[-1][x][y] - 1
                count.append(ct)
                M = max(M, *[ct[x][x] for x in chars])
        return M
