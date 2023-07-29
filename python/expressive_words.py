"""
Sometimes people repeat letters to represent extra feeling. For example:

    "hello" -> "heeellooo"
    "hi" -> "hiiii"

In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

    For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.

Return the number of query strings that are stretchy.
"""

from typing import List


class Solution:

    def expressiveWords(self, s: str, words: List[str]) -> int:
        ct = 0
        for w in words:
            # print(s, w)
            if self.can_stretch(w, s):
                ct += 1
        return ct

    def can_stretch(self, w1, w2):
        i1, i2 = 0, 0
        while i1 < len(w1):
            if i2 >= len(w2) or w2[i2] != w1[i1]:
                return False
            ct1 = 0
            ct2 = 0
            while i2 < len(w2) and w1[i1] == w2[i2]:
                i2 += 1
                ct2 += 1
            i2 -= 1
            while i1 < len(w1) and w1[i1] == w2[i2]:
                i1 += 1
                ct1 += 1
            i1 -= 1
            if ct1 != ct2:
                if ct2 < ct1 or ct2 < 3:
                    return False
            else:
                i1 += 1
                i2 += 1
        return i2 >= len(w2)
