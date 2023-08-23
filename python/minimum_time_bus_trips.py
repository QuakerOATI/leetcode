"""
Minimum Time to Complete Trips

You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.
"""

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """
        99.90 %ile runtime
        25.12 %ile memory
        """

        def numTrips(T):
            return sum([T//t for t in time])

        l, r = 1, min(time)*totalTrips
        while r > l:
            m = (r+l)//2
            if numTrips(m) < totalTrips:
                l = m + 1
            else:
                r = m
        return l
