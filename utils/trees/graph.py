from ..graph import *

def stringify_node_linewise(node, stalklength=2, flat_char="_", min_width=3):
    lines, pos = _stringify_node_linewise(node, stalklength, flat_char, min_width)
    return lines

def _stringify_node_linewise(node, stalklength=2, flat_char="_", min_width=3):
    from itertools import zip_longest
    if node is node._tree.SENTINEL or node is None:
        g = _graph(node)
        if len(g) % 2 == 0:
            g += " "
        return [g.center(min_width)], max(min_width//2 + 1, len(g)//2 + 1)
    else:
        root = _graph(node)
        l, r = [_stringify_node_linewise(n, stalklength, flat_char, min_width)
            for n in node._children]
        left, lpos = l
        right, rpos = r
        w_left, w_right = max(map(len, left)), max(map(len, right))
        w_tot = w_left + max(w_right, len(root)//2 + 1)
        if w_tot % 2 == 0:
            w_tot += 1
        pos = w_left + 1
        if len(right) > len(left):
            left.extend(["".ljust(w_left) for _ in range(len(right) - len(left))])
        root = root.center(2*pos - 1).ljust(w_tot)
        stalk = ["|".rjust(w_left + 1).ljust(w_tot) for _ in range(stalklength)]
        platform = "".ljust(lpos).ljust(w_left, flat_char) \
            + "|" \
            + "".ljust(rpos - 1, flat_char)
        platform = platform.ljust(w_tot)
        branches = [("|".rjust(lpos).ljust(w_left) + "|".rjust(rpos + 1)).ljust(w_tot)
            for _ in range(stalklength)]
        return [root, *stalk, platform, *branches,
                *map(lambda pair: " ".join([pair[0].ljust(w_left), pair[1].rjust(w_right)]).ljust(w_tot), 
                     zip_longest(left, right, fillvalue=""))], pos
