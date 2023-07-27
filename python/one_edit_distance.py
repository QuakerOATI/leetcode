"""
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

    Insert exactly one character into s to get t.
    Delete exactly one character from s to get t.
    Replace exactly one character of s with a different character to get t.
"""


class Solution:

    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        len(s) vs len(t)
        """
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)
        if len(t) == 0:
            return len(s) == 1
        if len(s) == len(t):
            # exactly one letter must differ
            return len([i for i in range(len(s)) if s[i] != t[i]]) == 1
        elif len(s) == len(t) + 1:
            if s[:len(t)] == t or s[1:] == t:
                return True
            for i in range(len(t)):
                if t[i] != s[i]:
                    break
            return t[i:] == s[i+1:]
        else:
            return False
