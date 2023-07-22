from bisect import bisect_right

class SnapshotArray:
    """Accepted, but oh my God is it bad compared to other solutions
    """
    def __init__(self, length: int):
        self._snap_id = 0
        self._array = [[[0], [0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        snap, oldval = self._array[index][0][-1], self._array[index][1][-1]
        if snap == self._snap_id:
            self._array[index][1][-1] = val
        else:
            self._array[index][0].append(self._snap_id)
            self._array[index][1].append(val)

    def snap(self) -> int:
        self._snap_id += 1
        return self._snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        ids, vals = self._array[index]
        j = max(bisect_right(ids, snap_id) - 1, 0)
        return vals[j]
