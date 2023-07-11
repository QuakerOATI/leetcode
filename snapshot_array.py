from bisect import bisect_right

class SnapshotArray:
    """TLE

    ["SnapshotArray","set","snap","set","get"]
    [[3],[0,5],[],[0,6],[0,0]]
    [null,null,0,null,5]

    ["SnapshotArray","set","snap","snap","set","set","get","get","get"]
    [[3],[1,6],[],[],[1,19],[0,4],[2,1],[2,0],[0,1]]
    [None,None,0,1,None,None,0,0,0]
    """
    def __init__(self, length: int):
        self._snap_id = 0
        self._array = [[(0, 0)]]

    def set(self, index: int, val: int) -> None:
        if self._array[index][-1][0] < self._snap_id:
            self._array[index].append((self._snap_id, val))
        else:
            self._array[index][-1] = (self._snap_id, val)

    def snap(self) -> int:
        self._snap_id += 1
        return self._snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect_right(self._array[index], (self._snap_id, self._snap_id))
        return self._array[index][i][1]
