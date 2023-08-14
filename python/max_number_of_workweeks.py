"""
There are n projects numbered from 0 to n - 1. You are given an integer array milestones where each milestones[i] denotes the number of milestones the ith project has.

You can work on the projects following these two rules:

Every week, you will finish exactly one milestone of one project. You must work every week.
You cannot work on two milestones from the same project for two consecutive weeks.
Once all the milestones of all the projects are finished, or if the only milestones that you can work on will cause you to violate the above rules, you will stop working. Note that you may not be able to finish every project's milestones due to these constraints.

Return the maximum number of weeks you would be able to work on the projects without violating the rules mentioned above.
"""
import heapq

class Solution:
    def numberOfWeeks(self, milestones):
        """
        83.19 %ile runtime
        17.65 %ile memory
        """
        S, M = sum(milestones), max(milestones)
        if 2*M > S:
            return 2*(S-M) + 1
        else:
            return S

    def numberOfWeeksGreedy(self, milestones: List[int]) -> int:
        """
        The most obvious greedy approach.  It's instructive to think about why this fails.
        """
        if len(milestones) == 0:
            return 0
        q = [-x for x in sorted(milestones, reverse=True)]
        tot = 0
        while len(q) > 1:
            M1, M2 = heapq.heappop(q), heapq.heappop(q)
            tot -= 2*M2
            if M1 < M2:
                heapq.heappush(q, M1 - M2)
        return tot + len(q)
