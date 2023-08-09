"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""

class Solution:
    """
    84.29 %ile runtime
    30.41 %ile memory
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        m, idx, total = 0, 0, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            total += g - c
            if total < m:
                m = total
                idx = i
        total = 0
        for i in range(len(gas)):
            total += gas[(idx + i) % len(gas)] - cost[(idx + i) % len(gas)]
            if total < 0:
                return -1
        return idx

    def canCompleteCircuitGreedy1(self, gas: List[int], cost: List[int]) -> int:
        """
        The obvious greedy solution, but it doesn't work.
        """
        i = min(range(len(gas)), key=lambda j: gas[j] - cost[j])
        total = 0
        for j in range(len(gas)):
            total += gas[(i + j) % len(gas)] - cost[(i + j) % len(gas)]
            if total < 0:
                return -1
        return i
