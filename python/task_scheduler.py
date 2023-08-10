"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
"""
from collections import Counter
import heapq

class Solution:
    def leastIntervalOptimal(self, tasks, n):
        """
        97.43 %ile runtime
        77.35 %ile memory
        """
        c = Counter(tasks)
        mode = c.most_common(1)[0][1]
        mode_mult = len([l for l in c if c[l] == mode])
        return max(len(tasks), (mode-1)*(n+1) + mode_mult)

    def leastIntervalPQueue(self, tasks, n):
        """
        69.68 %ile runtime
        12.06 %ile memory

        This works, but misses a stupidly obvious solution (see above).
        """
        if n == 0:
            return len(tasks)
        elif len(tasks) == 0:
            return 0
        q = list(map(lambda x: (-n, -x[1]), Counter(tasks).most_common()))
        T = 0
        while len(q) > n:
            items = []
            for i in range(n+1):
                items.append(heapq.heappop(q))
            floor = -q[0][1] if len(q) > 0 else 1
            inc = -items[n][1] - floor + 1
            T += inc*(n+1)
            for last, rem in items:
                if rem < -inc:
                    heapq.heappush(q, (last, rem+inc))
        while len(q) > 0:
            last, rem = heapq.heappop(q)
            T = max(T+1, last + n + 1)
            if rem < -1:
                heapq.heappush(q, (T, rem+1))
        return T

    def leastIntervalPQueue1(self, tasks: List[str], n: int) -> int:
        """
        First attempt at a PQueue solution.  Unfortunately, the simple queueing scheme I chose here doesn't work.
        """
        if n == 0:
            return len(tasks)
        elif len(tasks) == 0:
            return 0
        q = list(map(lambda x: (-n, -x[1], x[0]), Counter(tasks).most_common()))
        T = 0
        while len(q) > 0:
            last, rem, let = heapq.heappop(q)
            t_old = T
            T = max(T + 1, last + n + 1)
            print((["idle"]*(T - t_old - 1)).join("\n"))
            print(let)
            if rem < -1:
                heapq.heappush(q, (T, rem+1))
            else:
                print(f"    Done with letter {let}")
        return T

    def leastIntervalGreedy(self, tasks: List[str], n: int) -> int:
        """
        Fast, but it doesn't work.
        """
        if n == 0:
            return len(tasks)
        elif len(tasks) == 0:
            return 0
        c = list(map(lambda x: x[1], Counter(tasks).most_common()))
        total = 0
        for i, (c1, c2) in enumerate(zip(c, c[1:])):
            total += (c1 - c2)*max(n+1, i+1)
        return total + (c[-1]-1)*max(n+1, len(c)) + max(n, len(c))
