"""
There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

    Serve 100 ml of soup A and 0 ml of soup B,
    Serve 75 ml of soup A and 25 ml of soup B,
    Serve 50 ml of soup A and 50 ml of soup B, and
    Serve 25 ml of soup A and 75 ml of soup B.

When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.
"""


class Solution:
    transitions = [[100, 0], [75, 25], [50, 50], [25, 75]]

    def __init__(self):
        self.memo = {}

    def soupServings(self, n: int) -> float:
        # This is the key trick to avoid overflow/TLE
        # We're relying on the stated precision limit of "within 10**-5" here
        if n > 4800:
            return 1.0
        return self.dfs(n, n)

    def dfs(self, na, nb):
        if (na, nb) not in self.memo:
            if na <= 0:
                if nb <= 0:
                    return 0.5
                else:
                    return 1.0
            elif nb <= 0:
                return 0.0
            else:
                self.memo[na, nb] = sum(
                    self.dfs(na - da, nb - db)
                    for da, db in self.transitions) / 4.0
        return self.memo[na, nb]

    def soupServingsRecursive(self, na, nb, memo):
        """Max recursion depth exceeded"""
        if (na, nb) not in memo:
            if na <= 0:
                if nb <= 0:
                    return 0.5
                return 1.0
            elif nb <= 0:
                return 0.0
            tot = 0
            for da, db in self.transitions:
                tot += self.soupServingsRecursive(na + da, nb + db, memo)
            memo[na, nb] = tot / 4.0
        return memo[na, nb]
