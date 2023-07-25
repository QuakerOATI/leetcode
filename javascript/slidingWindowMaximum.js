// Unfortunately, this gets TLE'd.  Apparently O(n*lg(n)) is too slow.
var maxSlidingWindowSortedArray = function(nums, k) {
    if (k===0)
        return [];
    else if (nums.length == 0)
        return [];
    else if (nums.length == 1)
        return [...nums];
    let window = new SortedArray(nums.slice(0, k));
    let ret = [window.peek()];
    for (let i=k; i<nums.length; ++i) {
        window.remove(nums[i-k]);
        window.insert(nums[i]);
        ret.push(window.peek());
    }
    return ret;
}

var maxSlidingWindow = function(nums, k, hb=null, stopAt=Infinity) {
    var hb = new HeapBag((x, y) => y-x);
    var ret = [];
    for (let i=0; i<k; ++i) {
        hb.insert(nums[i]);
    }
    ret.push(hb.peekNext());
    let i = 0;
    while (i+k < nums.length) {
        hb.remove(nums[i]);
        hb.insert(nums[++i+k-1]);
        ret.push(hb.peekNext());
    }
    return ret;
}

class HeapBag {
    /*
     * Circular linked-list and heap node wrapped into one.
     */
    _Node(value, idx) {
        let ret = { value, idx };
        ret.next = ret;
        ret.prev = ret;
        return ret;
    }
    constructor(cmp) {
        this.cmp = cmp;
        this._heap = [];
        this._nodes = {};
    }
    insert(elem) {
        let node = this._Node(elem, this._heap.length);
        this._nodes[elem] = this._nodes[elem] ?? node;
        node.next = this._nodes[elem].next;
        node.prev = this._nodes[elem].prev;
        node.next.prev = node;
        node.prev.next = node;
        this._heap.push(node);
        this._upheap(node);
    }
    remove(elem) {
        return this._removeNode(this._nodes[elem]);
    }
    popNext() {
        return this._removeNode(this._heap[0]);
    }
    peekNext() {
        return this._heap[0]?.value;
    }
    // Private helper functions
    get _last() { return this._heap[this._heap.length - 1]; }
    _removeNode(node) {
        if (!node)
            return node;
        let last = this._last;
        this._exchange(node, last);
        let ret = this._heap.pop().value;
        if (last.idx < this._heap.length) {
            this._upheap(last);
        }
        if (node === node.next) {
            node.next = null;
            node.prev = null;
        } else {
            node.next.prev = node.prev;
            node.prev.next = node.next;
        }
        this._nodes[node.value] = node.next;
        node = null;
        return ret;
    }
    _downheap(node) {
        for (let m = this._minChild(node); m && (this.cmp(m.value, node.value) < 0); m = this._minChild(node)) {
            this._exchange(node, m);
        }
    }
    _upheap(node) {
        for (let p = this._parent(node); p && (this.cmp(node.value, p.value) < 0); p = this._parent(node)) {
            if (p === node)
                break;
            this._exchange(p, node);
        }
        this._downheap(node);
    }
    _min(n1, n2) {
        if (!n1)
            return n2;
        if (!n2)
            return n1;
        else
            return this.cmp(n1.value, n2.value) < 0 ? n1 : n2;
    }
    _parent(node) {
        if (node.idx === 0) {
            return undefined;
        }
        return this._heap[Math.floor((node.idx - 1)/2)];
    }
    _minChild(node) {
        return this._min(this._heap[2*node.idx+1], this._heap[2*node.idx+2]);
    }
    _exchange(n1, n2) {
        let [i1, i2] = [n1.idx, n2.idx];
        n1.idx = i2;
        n2.idx = i1;
        this._heap[n1.idx] = n1;
        this._heap[n2.idx] = n2;
    }
}

