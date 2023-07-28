"""
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are
sorted lexicographically
Lexicographically Smaller

A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alien language than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the shorter string is the lexicographically smaller one.
by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.
"""
from typing import List
from collections import Counter


class Solution:

    def alienOrder(self, words: List[str]) -> str:
        """
        Topological sort

        Accepted, with optimal runtime!
        """
        edges = {}
        priors = Counter(set.union(*map(set, words)))
        order = ""
        for w1, w2 in zip(words, words[1:]):
            # print(w1, w2)
            if w1.startswith(w2) and w1 != w2:
                return ""
            for c1, c2 in zip(w1, w2):
                # print(f"    {(c1, c2)}")
                if c1 != c2:
                    edges.setdefault(c1, set())
                    if c2 not in edges[c1]:
                        edges[c1].add(c2)
                        priors[c2] += 1
                    break
        while len(priors) > 0:
            # print(priors, edges)
            if priors.pop(last := min(priors, key=lambda k: priors[k])) > 1:
                return ""
            # print(f"    Last: {last}")
            order += last
            for c in edges.get(last, []):
                priors[c] -= 1
        return order
