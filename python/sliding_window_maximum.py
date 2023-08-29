class Solution:
    def maxSlidingWindowMinQueue(self, nums, k):
        """
        Better, but still shitty:
        6.44 %ile runtime
        48 %ile memory
        """
        mq = MinQueue(lambda x, y: y - x)
        ans = []
        for n in nums[:k]:
            mq.enqueue(n)
        ans.append(mq.getMin())
        for n in nums[k:]:
            mq.dequeue()
            mq.enqueue(n)
            ans.append(mq.getMin())
        return ans

    def maxSlidingWindowBinarySearch(self, nums: List[int], k: int) -> List[int]:
        """
        The first solution I came up with, before reading about min-queues.
        5 %ile runtime
        89.36 %ile memory
        """
        if k == len(nums):
            return [max(nums)]
        window = sorted(nums[:k])
        M = [window[-1]]
        for l, r in zip(nums, nums[k:]):
            window.pop(bisect_left(window, l))
            window.insert(bisect_left(window, r), r)
            M.append(window[-1])
        return M

class MinQueue:
    def __init__(self, cmp=None):
        if cmp is None:
            cmp = lambda x, y: x - y
        self._cmp = cmp
        self._s1, self._s2 = [], []
    
    def enqueue(self, elem):
        self._s1.append((elem, self._min(elem, self._minLeft)))

    def dequeue(self):
        self._restack()
        val, minVal = self._s2.pop()
        return val

    def getMin(self):
        return self._min(self._minLeft, self._minRight)

    @property
    def _minLeft(self):
        if len(self._s1) > 0:
            return self._s1[-1][1]
        else:
            return None

    @property
    def _minRight(self):
        if len(self._s2) > 0:
            return self._s2[-1][1]
        else:
            return None

    def _min(self, a, b):
        if a is None:
            return b
        elif b is None:
            return a
        elif self._cmp(a, b) > 0:
            return b
        else:
            return a

    def _restack(self):
        if len(self._s2) == 0:
            while len(self._s1) > 0:
                val, _ = self._s1.pop()
                self._s2.append((val, self._min(val, self._minRight)))

    def __len__(self):
        return len(self._s1) + len(self._s2)
