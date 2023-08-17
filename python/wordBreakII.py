"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

from bisect import bisect_left, bisect_right


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        99.14 %ile runtime
        21.16 %ile memory
        """

        def helper(i, sentence):
            for prefix in self.extractGlossedPrefixes(wordDict, s[i:]):
                sentence.append(prefix)
                if i + len(prefix) >= len(s):
                    yield list(sentence)
                yield from helper(i + len(prefix), sentence)
                sentence.pop()

        wordDict.sort()
        print(list(self.extractGlossedPrefixes(wordDict, s)))
        return list(map(" ".join, helper(0, [])))

    def findByPrefix(self, words, prefix):
        """Assumes words is sorted"""
        idx = bisect_left(words, prefix)
        while words[idx].startswith(prefix):
            yield words[idx]
            idx += 1

    def extractGlossedPrefixes(self, words, s):
        """Generates all prefixes of s in the sorted array words"""
        idx = bisect_right(words, s)
        for i in range(idx - 1, -1, -1):
            if words[i][0] < s[0]:
                break
            elif s.startswith(words[i]):
                yield words[i]
