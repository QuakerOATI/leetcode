from ..tree import RedBlackTree, graph, stringify_node_linewise
from math import log2

def test_rbtree(N, print_graph=True):
    t = RedBlackTree()
    for x in range(N):
        t.insert(x)
        assert isinstance(t.root, t._Node)
        assert not t.root.isred
        assert len(t) == x + 1
    if print_graph:
        try:
            graph(t)
        except Exception as e:
            print(f"Exception while graphing: {e}")
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
