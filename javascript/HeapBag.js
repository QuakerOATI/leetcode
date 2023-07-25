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
    constructor(cmp, debug=false) {
        this.cmp = cmp;
        this._heap = [];
        this._nodes = {};
        this.debug = function(fn, name, msgFunc) {
            let newFunc = function(...args) {
                if (msgFunc)
                    console.log(msgFunc(args));
                let ret = fn.bind(this)(...args);
                if (!this.checkHeap()) {
                    throw new Error(`Failed heap check after function call '${name}'`);
                }
                return ret;
            };
            newFunc.bind(this);
            return newFunc;
        };
        if (debug) {
            this.remove = this.debug(this.remove, "remove", (...args) => `Removing ${args[0]}...`);
            this.popNext = this.debug(this.popNext, "popNext");
            this.insert = this.debug(this.insert, "insert", (...args) => `Inserting ${args[0]}...`);
        }
    }
    insert(elem) {
        this._dumpHeapState("insert:begin");
        let node = this._Node(elem, this._heap.length);
        this._nodes[elem] = this._nodes[elem] ?? node;
        node.next = this._nodes[elem].next;
        node.prev = this._nodes[elem].prev;
        node.next.prev = node;
        node.prev.next = node;
        this._heap.push(node);
        this._upheap(node);
        this._dumpHeapState("insert:end")
    }
    remove(elem) {
        this._dumpHeapState("remove:begin");
        return this._removeNode(this._nodes[elem]);
    }
    popNext() {
        return this._removeNode(this._heap[0]);
    }
    peekNext() {
        return this._heap[0]?.value;
    }
    checkHeap() {
        if (this._heap.length === 0)
            return true;
        let pass = true;
        this._heap.forEach((n, i) => {
            for (let j of [2*i+1, 2*i+2]) {
                if (this._heap[j] && this.cmp(n.value, this._heap[j].value) > 0) {
                    console.log(`Nodes misordered at index ${i}: parent = ${n.value}, child = ${this._heap[j].value}`);
                    pass = false;
                }
            }
        });
        let claimedMin = this.peekNext();
        let actualMin = claimedMin;
        for (let n of this._heap) {
            if (this.cmp(n.value, actualMin) < 0) {
                actualMin = n.value;
                pass = false;
            }
        }
        console.log(`ACTUAL MIN:  ${actualMin}`);
        console.log(`CLAIMED MIN: ${claimedMin}`);
        console.log(pass ? "PASS" : "FAIL");
        return pass;
    }
    // Private helper functions
    get _last() { return this._heap[this._heap.length - 1]; }
    _removeNode(node) {
        this._dumpHeapState("_removeNode:begin");
        if (!node)
            return node;
        let last = this._last;
        if (!this._exchange(node, last)) {
            console.log(`Error while removing node with value ${node.value}`);
            return null;
        }
        let ret = this._heap.pop().value;
        //this.checkHeap();
        this._dumpHeapState("_removeNode:middle");
        if (last.idx < this._heap.length) {
            console.log(`       Downheaping (${last.idx}, ${last.value})...`);
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
        if (this._locate(node)) {
            for (let m = this._minChild(node); m && this.cmp(m.value, node.value) < 0; m = this._minChild(node)) {
                if (!this._exchange(node, m))
                    break;
            }
        }
    }
    _upheap(node) {
        if (this._locate(node)) {
            for (let p = this._parent(node); p && this.cmp(node.value, p.value) < 0; p = this._parent(node)) {
                if (p === node)
                    break;
                if (!this._exchange(node, p))
                    break;
            }
            this._downheap(node);
        }
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
        let [l, r] = [2*node.idx+1, 2*node.idx+2];
        return this._min(this._heap[l], this._heap[r]);
    }
    _exchange(n1, n2) {
        if (this._locate(n1) && this._locate(n2)) {
            let [i1, i2] = [n1.idx, n2.idx];
            n1.idx = i2;
            n2.idx = i1;
            this._heap[n1.idx] = n1;
            this._heap[n2.idx] = n2;
            return true;
        }
        return false;
    }
    _locate(node) {
        if (!node)
            return false;
        if (node.idx >= this._heap.length || this._heap[node.idx] !== node) {
            console.log(`Error locating node with value ${node.value} in HeapBag`);
            return false;
        }
        return true;
    }
    _dumpHeapState(loc) {
        console.log(`   Heap state @${loc}: ${this._heap.map(n => "(" + [n.idx, n.value].join(",") + ")").join(" ")}`);
    }
}

