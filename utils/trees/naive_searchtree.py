class NaiveSearchTree:
    """Minimal implementation of a self-balancing BST.

    Created for snapshot_array problem."""
    class _Node:
        _sentinel = None
        @classmethod
        def set_sentinel(cls, default):
            cls._sentinel = default
        def __init__(self, tree, value, weight=1, arity=2):
            self._tree = tree
            self.value = value
            self.weight = weight
            self.parent = self._sentinel
            self._children = [self._sentinel for _ in range(arity)]
        def update_weight(self):
            if self is self._sentinel:
                return
            else:
                self.weight = sum(map(lambda c: c.weight, self._children)) + 1
        def replace_child(self, c1, c2):
            self.replace_idx(self._children.index(c1), c2)
        def replace_idx(self, idx, c):
            old = self._children[idx]
            c.parent = self
            self._children[idx] = c
            self.update_weight()
            return old
        def get_child(self, idx):
            return self._children[idx]
        def add_child(self, node):
            idx = 0 if node.value < self.value else 1
            if (c := self.get_child(idx)) is self._sentinel:
                self.replace_idx(idx, node)
            else:
                c.add_child(node)
            self.update_weight()
        def bias(self, i, j):
            return self._children[i].weight - self._children[j].weight
        def __repr__(self):
            if self is self._sentinel:
                return f"{self.__class__}:SENTINEL"
            else:
                return f"[{self.__class__}:{self.value}]" + ":" + "".join([f"({repr(c)})" for c in self._children])

    def __init__(self, value):
        self.TERMINAL = self._Node(self, None, weight=0)
        self._Node.set_sentinel(self.TERMINAL)
        root = self._Node(self, value)
        self.TERMINAL.replace_idx(0, root)

    @property
    def root(self):
        return self.TERMINAL.get_child(0)

    def append(self, value):
        n = self._Node(self, value)
        self.root.add_child(n)
        self._balance(self.root)

    def _balance(self, node):
        if abs(b := node.bias(0, 1)) < 2:
            return
        self.rotate(node, int(b < 0))

    def rotate(self, node, idx):
        c = node.get_child(idx)
        if c is self.TERMINAL:
            return
        else:
            node.parent.replace_child(node, c)
            cc = c.replace_idx(idx-1, node)
            node.replace_idx(idx, cc)

    def height(self):
        r, h = self.root, 0
        while r is not self.TERMINAL:
            r = max(r._children, key=lambda c: c.weight)
            h += 1
        return h

    def __len__(self):
        return self.root.weight

    def __repr__(self):
        return repr(self.root)
