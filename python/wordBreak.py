"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wds = set(wordDict)
        dp = [0] * (len(s) + 1)
        for i, c in enumerate(s):
            for w in wds:
                if s[i:].startswith(w):
                    dp[i + len(w)] = max(dp[i + len(w)], dp[i] + len(w))
        return dp[-1] == len(s)
