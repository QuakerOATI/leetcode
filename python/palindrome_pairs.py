"""
You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:

0 <= i, j < words.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a 
palindrome
.
Return an array of all the palindrome pairs of words.
"""

from bisect import bisect_left

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        99.35 %ile runtime
        42.79 %ile memory
        """
        result = []
        S = sorted(zip(words, range(len(words))))
        R = sorted(zip([w[-1::-1] for w in words], range(len(words))))
        hasEmpty = S[0][0] == ""
        for i, w in enumerate(words):
            if hasEmpty and w == w[-1::-1] and i != (e := S[0][1]):
                result.extend([[i, e], [e, i]])
            r = w[-1::-1]
            iS = bisect_left(S, (r, i))
            iR = bisect_left(R, (w, i))
            while iS < len(words):
                wS, j = S[iS]
                if not wS.startswith(r):
                    break
                elif i != j and wS[len(w):] == wS[-1:len(w)-1:-1]:
                    result.append([j, i])
                iS += 1
            while iR < len(words):
                wR, j = R[iR]
                if not wR.startswith(w):
                    break
                elif i != j and wR[len(w):] == wR[-1:len(w)-1:-1]:
                    result.append([i, j])
                iR += 1
        return(result)
