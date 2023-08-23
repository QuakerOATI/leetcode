"""
You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.
"""

from math import ceil
from bisect import bisect_right

class Solution:
    """
    99.91 %ile runtime
    56.07 %ile memory
    """
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1
        elif len(dist) == 1:
            return ceil((100*dist[0]//hour)/100)
        last = dist.pop()
        dist.sort()
        M = max(last, dist[-1])
        def totalTime(speed):
            total = 0
            for d in range(0, M, speed):
                idx = bisect_right(dist, d)
                total += len(dist) - idx
            return total + last/speed
        l, r = 1, M
        while r > l:
            v = (r+l)//2
            if totalTime(v) > hour:
                l = v + 1
            else:
                r = v
        if totalTime(l) > hour:
            return ceil((100*last//(hour - len(dist)))/100)        
        return l
