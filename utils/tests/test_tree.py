from ..trees.bst import RedBlackTree
from ..graph import graph
from ..trees.graph import stringify_node_linewise
from math import log2
from random import randint, choice
from ..test import test_assert

def test_rbtree(num_inserts=500, keys=range(1000), values=range(1000), print_graph=False):
    t = RedBlackTree()
    d = {}
    for x in range(num_inserts):
        key, val = choice(keys), choice(values)
        t[key] = val
        d[key] = val
        test_assert("RBTree t: class(t.root) == t._Node", isinstance, t.root, t._Node)
        test_assert("RBTree t: t.root is black", lambda t: not t.root.isred, t)
        test_assert("RBTree t: len(t) == {1} after insert", lambda _t, _x: len(_t) == _x, t, len(d))
        test_assert("RBTree t: {1} in t after insert", lambda _t, _x: _x in _t, t, key)
        test_assert("RBTree t: t[{1}] == {2} after insert", lambda _t, _k, _v: _t[_k] == _v, t, key, val)
    for key, val in d.items():
        test_assert("RBTree t: t[{1}] == {2} after all inserted", lambda _t, _k, _v: _t[_k] == _v, t, key, val)
    if print_graph:
        try:
            graph(t)
        except Exception as e:
            print(f"Exception while graphing: {e}")
    is_rbtree(t)
    return t

def is_rbtree(tree: RedBlackTree):
    re = _find_rederror(tree.root)
    if re is not None:
        print(f"Rederror found at node {re}:")
        print("\n".join(stringify_node_linewise(re)))
    bhs = _blackheight(tree.root)
    if len(bhs) > 1:
        print(f"More than one blackheight from root was found: {list(bhs)}")
    max_height = 2*log2(len(tree) + 1)
    if (h := tree.height()) > max_height:
        print(f"Tree height {h} exceeds maximum theoretical height {max_height}")
    if (N := _num_childnodes(tree.root)) != len(tree):
        print(f"{N} nodes found ({len(tree)} expected)")

def _find_rederror(node: RedBlackTree._Node):
    if node is not node._tree.SENTINEL:
        l, r = node._children
        if node.isred:
            if l.isred or r.isred:
                return node
        le, re = _find_rederror(l), _find_rederror(r)
        if le is not None:
            return le
        elif re is not None:
            return re
    elif node.isred:
        return node
    return None

def _blackheight(node: RedBlackTree._Node):
    hs = set()
    stack = [(0, node)]
    while len(stack) > 0:
        l, n = stack.pop()
        if n is node._tree.SENTINEL:
            hs.add(l)
            continue
        elif not n.isred:
            l += 1
        stack.extend([(l, c) for c in n._children])
    return hs

def _num_childnodes(node: RedBlackTree._Node):
    N = 0
    stack = [node]
    while len(stack) > 0:
        n = stack.pop()
        if n is node._tree.SENTINEL:
            continue
        stack.extend(n._children)
        N += 1
    return N
