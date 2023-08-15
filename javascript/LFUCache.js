/*
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.
*/



/**
 * @param {number} capacity
 */
var LFUCache = function(capacity) {
    this.capacity = capacity;
    this.heap = new Heap();
    this.map = {};
};

/** 
 * @param {number} key
 * @return {number}
 */
LFUCache.prototype.get = function(key) {
    console.groupCollapsed(`GET: ${key}`);
    let node = this.map[key];
    if (node == null) {
        console.log("Not found");
        console.groupEnd();
        return -1;
    }
    this.heap.remove(node);
    this.heap.insert(node.touch());
    console.log(`   --> ${node.value}`);
    console.groupEnd();
    return node.value;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LFUCache.prototype.put = function(key, value) {
    console.groupCollapsed(`PUT: ${key}, ${value}`);
    let node = this.map[key];
    if (node == null) {
        node = new HeapNode(key, value);
        if (this.heap.size >= this.capacity) {
            let removed = this.heap.pop();
            delete this.map[removed.key];
            delete removed;
        }
        this.heap.insert(node);
        this.map[key] = node;
    } else {
        node.value = value;
        this.heap.insert(this.heap.remove(node).touch());
    }
    console.groupEnd();
};

/** 
 * Your LFUCache object will be instantiated and called as such:
 * var obj = new LFUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

var HeapNode = function(key, value) {
    this.key = key;
    this.value = value;
    this.parent = null;
    this.left = null;
    this.right = null;
    this.frequency = 1;
    this.lastUsed = Date.now();
};

HeapNode.prototype.touch = function() {
    console.group(`TOUCH: ${this}`);
    ++this.frequency;
    this.lastUsed = Date.now();
    console.groupEnd();
    return this;
};

HeapNode.prototype.cmp = function(other) {
    return this.frequency === other.frequency
        ? this.lastUsed - other.lastUsed
        : this.frequency - other.frequency;
};

HeapNode.prototype.leastChild = function() {
    return [this.left, this.right].filter(c => c)
        .reduce((m, c) => !m || c.cmp(m) < 0 ? c : m, null);
};

HeapNode.prototype.sibling = function() {
    return this === this.parent?.left ? this.parent?.right : this.parent?.left;
};

HeapNode.prototype.addChild = function(c) {
    console.group(`ADD CHILD: parent = ${this}, child = ${c}`);
    if (c == null) {
        console.groupEnd();
        return;
    }
    if (this.left == null)
        this.left = c;
    else if (this.right == null)
        this.right = c;
    else 
        throw new Error(`Parent node ${this} cannot accept another child ${c}`);
    c.parent = this;
    console.groupEnd();
    return this;
};

HeapNode.prototype.removeChild = function(c) {
    console.group(`REMOVE CHILD: parent = ${this}, child = ${c}`);
    if (c == null) {
        console.groupEnd();
        return;
    }
    if (c === this.left)
        this.left = null;
    else if (c === this.right)
        this.right = null;
    else
        throw new Error(`Cannot find child-node ${c} from parent ${this}`);
    c.parent = null;
    console.groupEnd();
    return c;
};

var Heap = function() {
    this.root = null;
    this.tail = null;
    this.size = 0;
};

HeapNode.prototype.toString = function() {
    return `(${this.key}, ${this.value})`;
};

Heap.prototype.insert = function(node) {
    console.group(`INSERT: ${node}`);
    //this.printState("Before");
    if (this.root == null) {
        node.parent = null;
        this.root = node;
        this.tail = this.root;
        this.size = 1;
    } else {
        try {
            this.tail.parent.addChild(node);
        }
        catch (err) {
            console.log(`Tried adding child ${node} to tail ${this.tail}`);
            console.log(`\tAdding child to tail ${this.tail} instead`);
            this.tail.addChild(node);
        }
        this.tail = node;
        this.upheap(node);
        this.downheap(node);
        ++this.size;
    }
    //this.printState("After");
    console.groupEnd();
    return node;
};

Heap.prototype.remove = function(node) {
    console.group(`REMOVE: ${node}`);
    //this.printState("Before");
    if (node === this.tail) {
        this.tail = this.tail.sibling() ?? this.tail.parent;
        console.log(`REDEF TAIL: ${node} --> ${this.tail}`);
        node.parent?.removeChild(node);
        if (node === this.root)
            this.root = null;
    } else {
        let t = this.tail;
        this.swap(node, t);
        this.tail = node.sibling() ?? node.parent;
        node.parent?.removeChild(node);
        this.downheap(t);
    }
    console.assert(node.left == null && node.right == null, `Node ${node} shouldn't have non-null children`);
    --this.size;
    //this.printState("After");
    console.groupEnd();
    return node;
};

Heap.prototype.pop = function() {
    console.group(`POP: ${this.root}`);
    console.groupEnd();
    return this.remove(this.root);
};

Heap.prototype.upheap = function(node) {
    console.group(`UPHEAP: ${node}`);
    //this.printState("Before");
    if (node === this.root || node.parent == null) {
        console.groupEnd();
        return node;
    }
    for (let p = node.parent; p && node.cmp(p) < 0; p = node.parent)
        this.swap(p, node);
    //this.printState("After");
    console.groupEnd();
    return node;
};

Heap.prototype.downheap = function(node) {
    console.group(`DOWNHEAP: ${node}`);
    //this.printState("Before");
    if (node === this.tail || node.leastChild() == null) {
        console.groupEnd();
        return node;
    }
    for (let c = node.leastChild(); c && c.cmp(node) < 0; c = node.leastChild())
        this.swap(c, node);
    //this.printState("After");
    console.groupEnd();
    return node;
};

Heap.prototype.swap = function(n1, n2) {
    console.group(`SWAP: ${n1} <--> ${n2}`);
    //this.printState("Before");
    if (n1 === n2) {
        console.groupEnd();
        return;
    }
    let [p1, p2] = [n1, n2].map(n => n.parent);
    let [c1, c2] = [n1, n2].map(n => 
        [n.removeChild(n.left), n.removeChild(n.right)]);
    if (p1 == null) {
        this.root = n2;
    } 
    if (p2 == null) {
        this.root = n1;
    } 
    if (p1 !== n2) {
        p1?.removeChild(n1);
        p1?.addChild(n2);
    } else {
        n1.addChild(n2);
    } 
    if (p2 !== n1) {
        p2?.removeChild(n2);
        p2?.addChild(n1);
    } else {
        n2.addChild(n1);
    }
    c2.filter(c => c !== n1).forEach(c => n1.addChild(c));
    c1.filter(c => c !== n2).forEach(c => n2.addChild(c));
    if (n1 === this.tail) {
        this.tail = n2;
    } else if (n2 === this.tail) {
        this.tail = n1;
    }
    //this.printState("After");
    console.groupEnd();
};

Heap.prototype.printState = function(msg) {
    console.group(`Heap state: ${msg ?? ""}`);
    console.table(this, ["key", "value", "frequency"]);
    console.groupEnd();
};

Heap.prototype.check = function() {
    var checkNode = function(n) {
        [n.left, n.right].filter(x => x).forEach(x => {
            console.assert(n.cmp(x) <= 0, `Parent node ${n} is > child node ${x}`);
            checkNode(x);
        });
    };
    checkNode(this.root);
};

