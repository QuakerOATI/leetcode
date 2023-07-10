from collections import namedtuple
from utils.trees.bst import RedBlackTree

class SnapshotArray:
    """TLE"""

    Momnt = namedtuple("Moment", ["snap_id", "value"])

    def __init__(self, length: int): 
        self._snaps = 0
        self._array = [self.Moment(0, 0) for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self._array[index].value = val

    def snap(self) -> int:
        self._snaps += 1
        return self._snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        moment = self._array[index][-1]
        
    def _rectify(self, index):
        elems = self._array[index]
        if (l := len(elems)) < self._snaps + 1:
            elems.extend([elems[-1] for _ in range(self._snaps - l + 1)])

    def __len__(self):
        return len(self._array)

    @property
    def num_snaps(self):
        """The num_snaps property."""
        return self._snaps
    
    def __repr__(self):
        return repr(self._array)

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
