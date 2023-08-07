class SolutionIII:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. You may complete at most two transactions.

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
    """

    def maxProfit(self, prices):
        left, right = [0], [0]
        rMax, lMin = prices[-1], prices[0]
        for i in range(len(prices)):
            rMax = max(rMax, prices[-i - 1])
            lMin = min(lMin, prices[i])
            left.append(max(left[-1], prices[i] - lMin))
            right.append(max(right[-1], rMax - prices[-i - 1]))
        best = 0
        left.pop(0)
        right.pop(0)
        print(left, right)
        for i in range(len(prices)):
            best = max(best, left[i] + right[len(prices) - i - 1])
        return best

    def maxProfitTLE(self, prices):
        """
        DP recursion: 
            dp[i][j][k] = max(dp[i][r][k1] + dp[r+1][j][k - k1], i <= r <= j, 0 < k1 <= k)
            dp[i][j][2] = max(dp[i][j][1], dp[i][r][1] + dp[r+1][j][1] for i < j <= k)

        >>> s = Solution()
        >>> Solution.maxProfit([1,2,4,2,5,7,2,4,9,0])
        13
        """

        def maxProfitOneTransaction(priceIntervals):
            if len(priceIntervals) < 1:
                return 0
            m = priceIntervals[0][0]
            best = 0
            for i in priceIntervals:
                m = min(i[0], m)
                best = max(i[1] - m, best)
            return best

        prices.append(-1)
        prev = prices[0]
        int_min = prev
        intervals = []
        for p in prices[1:]:
            if p < prev:
                intervals.append((int_min, prev))
                int_min = p
            prev = p
        print(intervals)
        return max(
            maxProfitOneTransaction(intervals[:k]) +
            maxProfitOneTransaction(intervals[k:])
            for k in range(len(intervals)))


class SolutionCooldown:

    def maxProfit(self, prices):
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

        After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

        Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
        """
        if len(prices) < 3:
            return max(prices[-1] - prices[0], 0)

        onOrBefore, onOrAfter = [0], []

        for p, prev in zip(prices[1:], prices):
            if p > prev:

        onOrBefore, onOrAfter = [0], [0]
        minLeft, maxRight = prices[0], prices[-1]
        countLeft, countRight = 0, 0
        for i in range(1, len(prices) - 1):
            l, r, pl, pr = prices[i], prices[-i - 1], prices[i - 1], prices[-i]
            if l > pl:
                countLeft += l - pl
            elif l < pl:
                countLeft = onOrBefore[-1]
            onOrBefore.append(countLeft)
            if r < pr:
                countRight += pr - r
            elif r > pr:
                countRight = onOrAfter[0]
            onOrAfter.insert(0, countRight)
        onOrBefore.pop(0)
        onOrAfter.pop()
        onOrAfter.extend([0, 0])
        return max(map(sum, zip(onOrBefore, onOrAfter[2:])))
