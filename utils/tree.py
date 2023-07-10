from .well_ordered import WellOrdered

def _graph(obj):
    if hasattr(obj, "__graph__"):
        if callable(obj.__graph__):
            return obj.__graph__()
        else:
            return repr(obj.__graph__)
    else:
        raise AttributeError(f"Object {obj} does not implement __graph__()")

def graph(obj):
    print(_graph(obj))

def _stringify_node_linewise(node, stalklength=2, flat_char="_", min_width=3):
    from itertools import zip_longest
    if node is node._tree.SENTINEL or node is None:
        return [_graph(node).center(min_width)]
    else:
        root = _graph(node)
        left, right = (_stringify_node_linewise(n, stalklength, flat_char, min_width)
            for n in node._children)
        w_left, w_right = len(left[0]), len(right[0])
        w_tot = w_left + max(w_right, len(root)//2 + 1)
        if len(right) > len(left):
            left.extend(["".ljust(w_left) for _ in range(len(right) - len(left))])
        root = root.center(2*w_left + 1).ljust(w_tot)
        stalk = ["|".rjust(w_left + 1).ljust(w_tot) for _ in range(stalklength)]
        platform = flat_char.rjust(w_left//2 + 1).ljust(w_left, flat_char) \
            + "|" \
            + flat_char.ljust(w_right//2 + 1, flat_char)
        platform = platform.ljust(w_tot)
        branches = [("|".center(w_left + 1) + "|".center(w_right)).ljust(w_tot)
            for _ in range(stalklength)]
        return [root, *stalk, platform, *branches, *map(lambda pair: " ".join(pair).ljust(w_tot), zip_longest(left, right, fillvalue=""))]

class TreeException(Exception):
    pass

class EmptyTreeException(TreeException):
    pass

class BinarySearchTree:
    class _Node(WellOrdered):
        def __init__(self, tree, value, parent, left, right):
            self._tree = tree
            self._value = value
            self._parent = parent
            self._children = [left, right]

        def __repr__(self):
            if self is self._tree.SENTINEL:
                return f"{self.__class__}:SENTINEL"
            else:
                return f"[{self.__class__}:{self._value}]" + ":" + "".join([f"({repr(c)})" for c in self._children])

        def __graph__(self, stalklength=2, flat_char="_"):
            if self is self._tree.SENTINEL:
                return "*"
            return f"({self._value})"

        def __eq__(self, other):
            return self._tree is other._tree and self._value == other._value

        def __lt__(self, other):
            if self._tree is not other._tree:
                return False
            elif self is self._tree.SENTINEL:
                return True
            elif other is self._tree.SENTINEL:
                return False
            else:
                return self._value < other._value

        def _checktype(self, *others):
            for other in others:
                if not isinstance(other, self.__class__):
                    raise TreeException(f"Attempted {self.__class__} operation with operand of type {other.__class__}")

        def _get_index(self, obj):
            return int(obj) % 2

        def get_child(self, idx):
            return self._children[self._get_index(idx)]

        def replace_child(self, n1, n2):
            self._checktype(n1, n2)
            b = n1.birthday
            if self.get_child(b) is not n1:
                raise TreeException("Attempted to replace a non-child node")
            self.set_child(n1.birthday, n2)

        def set_child(self, idx, node):
            self._checktype(node)
            ret = self.get_child(idx)
            self._children[self._get_index(idx)] = node
            if node is not self._tree.SENTINEL:
                node._parent = self
            return ret

        @property
        def birthday(self):
            if self is self._tree.SENTINEL:
                return -1
            # Can't use self._parent._children.index(self) because of _Node.__eq__ implementation
            for b in 0, 1:
                if self is self._parent._children[b]:
                    return b

        @property
        def left(self):
            return self.get_child(0)

        @property
        def right(self):
            return self.get_child(1)

    def __init__(self):
        self.SENTINEL = self._Node(self, None, None, None, None)
        self._root = None
        self._sz = 0

    def __repr__(self):
        return repr(self.root)

    def __graph__(self, stalklength=2, flat_char="_", min_width=3):
        if len(self) == 0:
            return "<Empty>"
        return "\n".join(_stringify_node_linewise(self.root, stalklength, flat_char, min_width))

    def _create_node(self, value):
        return self._Node(self, value, self.SENTINEL, self.SENTINEL, self.SENTINEL)

    def _rotate(self, node, idx):
        c = node.get_child(idx-1)
        if c is self.SENTINEL:
            raise TreeException("Cannot rotate at leaf node")
        # node.set_child(idx-1, c.get_child(idx))
        (p := node._parent).replace_child(node, c)
        orphan = c.set_child(idx, node)
        node.set_child(idx-1, orphan)
        if p is self.SENTINEL:
            self._root = c

    def rotate_left(self, node):
        self._rotate(node, 0)

    def rotate_right(self, node):
        self._rotate(node, 1)

    def _get_pred(self, value):
        prev, curr = self.SENTINEL, self.root
        while curr is not self.SENTINEL and curr is not None:
            prev = curr
            curr = curr.get_child(value > curr._value)
        return prev

    def _insert_node(self, node):
        self.SENTINEL._checktype(node)
        p = self._get_pred(node._value)
        p.set_child(node > p, node)
        if p is self.SENTINEL:
            self._root = node
        self._sz += 1

    @property
    def root(self):
        return self._root

    def insert(self, value):
        self._insert_node(self._create_node(value))

    def get_pred(self, value):
        if len(self) <= 0:
            raise EmptyTreeException("Cannot find predecessor in empty tree")
        return self._get_pred(value)

    def __len__(self):
        return self._sz

class RedBlackTree(BinarySearchTree):
    class _Node(BinarySearchTree._Node):
        def __init__(self, *args, isred=True):
            super().__init__(*args)
            self._isred = isred

        def __graph__(self):
            ret = super().__graph__()
            if self.isred:
                ret = ret.replace("(", "[").replace(")", "]")
            return ret

        def color_black(self):
            self._isred = False

        def color_red(self):
            self._isred = True

        @property
        def isred(self):
            return self._isred

    def __init__(self):
        super().__init__()
        self._root = None

    def insert(self, value):
        super()._insert_node(node := (self._create_node(value)))
        assert isinstance(node, self._Node)
        self._recolor(node)

    def _recolor(self, node):
        """See CLRS, c13, pp309-322."""
        if node is self.root:
            node.color_black()
            return
        while node._parent.isred:
            pbd = (p := node._parent).birthday
            uncle = (pp := p._parent).get_child(pbd - 1)
            if uncle.isred:
                p.color_black()
                uncle.color_black()
                pp.color_red()
                node = pp
            else:
                # The loop is guaranteed to terminate in this case
                if node.birthday != pbd:
                    # Rotate node into node._parent and set node --> node._parent
                    # This way, we ensure that node.birthday == pbd, falling into the last case
                    node = p
                    self._rotate(node, pbd)
                # Note: node._parent may not be the same as p here, but pp is guaranteed to be the same
                (p := node._parent).color_black()
                pp.color_red()
                self._rotate(pp, pbd-1)
        self.root.color_black()

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
