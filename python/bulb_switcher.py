"""
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

|{x <= n : numProperDivisors(x) % 2 === 0}|

precompute primes up to 10**9

[n/4, n/2]
[n/]
"""

from math import sqrt, floor


class Solution:

    def bulbSwitch(self, n: int) -> int:
        return floor(sqrt(n))
