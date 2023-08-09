"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""

class Solution:
    """
    64.88 %ile runtime
    93.40 %ile memory

    There exists a neater dynamic programming solution, but this one isn't too bad despite its ugliness.
    """
    def candy(self, ratings: List[int]) -> int:
        def sgn(x):
            if x == 0: return 0
            elif x < 0: return -1
            return 1

        total = 0
        while len(ratings) > 1:
            if ratings[-1] == ratings[-2]:
                total += 1
                ratings.pop()
            elif ratings[0] == ratings[1]:
                total += 1
                ratings.pop(0)
            else:
                break

        if len(ratings) == 0:
            return total
        if len(ratings) == 1:
            return total + 1
        if len(ratings) == 2:
            return total + 3

        diffs = [0, sgn(ratings[1] - ratings[0])]
        for i in range(2, len(ratings)):
            p1, p2, r = ratings[i-2:i+1]
            if r == p2:
                diffs.append(0)
            elif sgn(r - p2) == sgn(p2 - p1):
                diffs[-1] += sgn(diffs[-1])
            else:
                diffs.append(sgn(r - p2))
        diffs.append(0)
        
        for d, dnext, dprev in zip(diffs[1:], diffs[2:], diffs):
            if d == 0:
                if dnext == 0:
                    total += 1
                continue 
            if (d > 0 and d <= abs(dnext)) or (d < 0 and abs(d) < dprev):
                total  -= abs(d) + 1
            if d < 0 and dnext > 0:
                total -= 1
            d = abs(d) + 1
            total += d*(d+1)//2
        return total 
