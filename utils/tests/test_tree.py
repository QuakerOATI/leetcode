from ..tree import RedBlackTree, graph

def test_rbtree(N):
    t = RedBlackTree()
    for x in range(N):
        t.insert(x)
        assert isinstance(t.root, t._Node)
        assert not t.root.isred
        assert len(t) == x + 1
    try:
        graph(t)
    except Exception as e:
        print(f"Exception while graphing: {e}")
    return t


