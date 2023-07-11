from utils.trees.bst import RedBlackTree as RBTree
from utils.graph import graph

class BinarySearchTree:
    class _Node:
        def __init__(self, tree, key, value, parent, left, right):
            self._tree = tree
            self.key = key
            self.value = value
            self.parent = parent
            self._children = [left, right]

        def __eq__(self, other):
            return self._tree is other._tree and self.key == other.key

        def __lt__(self, other):
            if self._tree is not other._tree:
                return False
            elif self is self._tree.SENTINEL:
                return True
            elif other is self._tree.SENTINEL:
                return False
            else:
                return self.key < other.key

        def __gt__(self, other):
            return not self == other and not self < other

        def _get_index(self, obj):
            return int(obj) % 2

        def get_child(self, idx):
            return self._children[self._get_index(idx)]

        def replace_child(self, n1, n2):
            b = n1.birthday
            self.set_child(n1.birthday, n2)

        def set_child(self, idx, node):
            ret = self.get_child(idx)
            self._children[self._get_index(idx)] = node
            if node is not self._tree.SENTINEL:
                node.parent = self
            return ret

        @property
        def birthday(self):
            if self is self._tree.SENTINEL:
                return -1
            for b in 0, 1:
                if self is self.parent._children[b]:
                    return b

    def __init__(self):
        self.SENTINEL = self._Node(self, None, None, None, None, None)
        self._root = None
        self._sz = 0

    def _create_node(self, key, value):
        return self._Node(self, key, value, self.SENTINEL, self.SENTINEL, self.SENTINEL)

    def _rotate(self, node, idx):
        c = node.get_child(idx-1)
        if c is self.SENTINEL:
            raise TreeException("Cannot rotate at leaf node")
        # node.set_child(idx-1, c.get_child(idx))
        (p := node.parent).replace_child(node, c)
        orphan = c.set_child(idx, node)
        node.set_child(idx-1, orphan)
        if p is self.SENTINEL:
            self._root = c

    def _insert_node(self, node):
        p = self._get_pred(node.key, require_leaf=True)
        p.set_child(node > p, node)
        if p is self.SENTINEL:
            self._root = node
        self._sz += 1

    @property
    def root(self):
        return self._root

    def get_pred(self, key):
        if len(self) <= 0:
            raise EmptyTreeException("Cannot find predecessor in empty tree")
        return self._get_pred(key, require_leaf=False).value

    def _get_pred(self, key, require_leaf=True):
        prev, curr = self.SENTINEL, self.root
        while curr is not self.SENTINEL and curr is not None:
            prev = curr
            curr = curr.get_child(key > curr.key)
            if prev.key == key and not require_leaf:
                return prev
        return prev

    def __setitem__(self, key, value):
        n = self._get_pred(key, require_leaf=False)
        if n.key == key:
            n.value = value
        else:
            node = self._create_node(key, value)
            self._insert_node(node)

    def __len__(self):
        return self._sz

    def __contains__(self, key):
        p = self._get_pred(key, require_leaf=False)
        return p is not self.SENTINEL and p is not None and p.key == key

    def __getitem__(self, key):
        p = self._get_pred(key, require_leaf=False)
        if p is self.SENTINEL or p is None or p.key != key:
            raise KeyError(f"Key {key} not found")
        return p.value

class RedBlackTree(BinarySearchTree):
    class _Node(BinarySearchTree._Node):
        def __init__(self, *args, isred=True):
            super().__init__(*args)
            self._isred = isred

        def color_black(self):
            self._isred = False

        def color_red(self):
            self._isred = True

        @property
        def isred(self):
            return self._isred

    def __init__(self):
        super().__init__()
        self.SENTINEL.color_black()

    def _insert_node(self, node):
        super()._insert_node(node)
        self._recolor(node)

    def _recolor(self, node):
        """See CLRS, c13, pp309-322."""
        if node is self.root:
            node.color_black()
            return
        while node.parent.isred:
            pbd = (p := node.parent).birthday
            uncle = (pp := p.parent).get_child(pbd - 1)
            if uncle.isred:
                p.color_black()
                uncle.color_black()
                pp.color_red()
                node = pp
            else:
                # The loop is guaranteed to terminate in this case
                if node.birthday != pbd:
                    # Rotate node into node.parent and set node --> node.parent
                    # This way, we ensure that node.birthday == pbd, falling into the last case
                    node = p
                    self._rotate(node, pbd)
                # Note: node.parent may not be the same as p here, but pp is guaranteed to be the same
                (p := node.parent).color_black()
                pp.color_red()
                self._rotate(pp, pbd-1)
        self.root.color_black()

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
        self._snaps = 0
        self._array = []
        for _ in range(length):
            rbt = RBTree()
            rbt[0] = 0
            self._array.append(rbt)

    def set(self, index: int, val: int) -> None:
        self._array[index][self._snaps] = val

    def snap(self) -> int:
        self._snaps += 1
        return self._snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        return self._array[index].get_pred(snap_id)
        
    def __len__(self):
        return len(self._array)

    @property
    def num_snaps(self):
        """The num_snaps property."""
        return self._snaps
    
    def __repr__(self):
        return repr(self._array)

    @classmethod
    def run_testcase(cls, funcs, args, expected, illustrate=False):
        ret = []
        if funcs.pop(0) == "SnapshotArray":
            sa = cls(*args.pop(0))
            try:
                ret.append(None)
                for method, xs in zip(funcs, args):
                    r = sa.__getattribute__(method)(*xs)
                    ret.append(r)
                    if illustrate:
                        print("="*50)
                        print(f"{method.upper()}{tuple(xs)} --> {r}")
                        print("-"*25)
                        for t in sa._array:
                            graph(t)
                        print("="*50)
                if ret != expected:
                    print("FAILED")
                    print(f"    Expected: {expected}")
                    print(f"    Returned: {ret}")
                else:
                    print("SUCCESS")
            except Exception as e:
                print(f"EXCEPTION: {e}")
            finally:
                return sa
        else:
            print("Test type unknown")
