from typing import List
from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """TLE
        Quadratic
        """
        ret = set()
        for shift in range(1, len(s) - 9):
            for j in range(len(s) - shift - 9):
                if s[j : j + 10] == s[j + shift : j + shift + 10]:
                    ret.add(s[j : j + 10])
        return list(ret)

    def findRepeatedDnaSequencesHashmap(self, s: str) -> List[str]:
        """Accepted"""
        if len(s) <= 10:
            return []
        c = Counter(s[i : i + 10] for i in range(len(s) - 9))
        return [sub for sub in c if c[sub] > 1]
