class Solution:
    """
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

    The matching should cover the entire input string (not partial).
    Note that we can assume the passed regex to be valid.
    """

    TERMINAL = object()

    class RegexError(Exception):
        pass

    def __init__(self):
        self.starred = None
        self.starct = 0
        self.matched = []

    def isMatch(self, s: str, p: str) -> bool:
        if "*" in p:
            return self.match_starred(s, p)
        else:
            return self.match_strict(s, p)

    def match_starred(self, s, p):
        segments = p.split("*")
        try:
            for seg in segments:
                for m in seg[:-1]:
                    s = self.consume_starred(s, m, False)
                s = self.consume_starred(s, seg[-1], True)
            return True
        except self.RegexError:
            return False

    def match_strict(self, s, p):
        try:
            for m in p:
                s = self.consume_strict(s, m)
            return True
        except self.RegexError:
            return False

    def consume_strict(self, s, meta):
        if len(s) == 0:
            raise self.RegexError()
        if not self.match_char(s[0], meta):
            raise self.RegexError()
        else:
            return s[1:]

    def consume_starred(self, s, meta, is_starred=False):
        if is_starred:
            ...
        if len(s) == 0:
            if is_starred:
                return ""
            elif self.match_char(meta, self.starred) and self.starct > 0:
                self.starct -= 1
                return ""
            else:
                raise self.RegexError()
        if self.match_char(self.starred, s[0]):
            ret = s.lstrip(self.starred)
            return ret, (self.starred, self.starct + len(s) - len(ret))

    def match_char(self, c1, c2):
        return c1 == c2 or c1 == "." or c2 == "."
