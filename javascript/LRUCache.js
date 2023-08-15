/*
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
*/

/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    // 94.44 %ile runtime
    // 86.20 %ile memory
    this.capacity = capacity;
    this.items = new CircularLinkedListNode(null, null);
    this.size = 0;
    this.map = {};
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    let node = this.map[key];
    if (node) {
        node.splice().insertBefore(this.items);
    }
    return node?.value ?? -1;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if (this.map.hasOwnProperty(key)) {
        let node = this.map[key];
        node.value = value;
        node.splice().insertBefore(this.items);
    } else {
        let node = new CircularLinkedListNode(key, value);
        if (++this.size > this.capacity) {
            this.size = this.capacity;
            let removed = this.items.next;
            // Behaves strangely if this.capacity === 0
            if (removed !== this.items) {
                removed = removed.splice();
                delete this.map[removed.key];
                delete removed;
            }
        }
        node.insertBefore(this.items);
        this.map[key] = node;
    }
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */

function CircularLinkedListNode(key, value, next=null, prev=null) {
    this.key = key;
    this.value = value;
    this.next = next == null ? this : next;
    this.prev = prev == null ? this : prev;
}

CircularLinkedListNode.prototype.splice = function() {
    if (this.prev)
        this.prev.next = this.next;
    if (this.next)
        this.next.prev = this.prev;
    return this;
}

CircularLinkedListNode.prototype.insertBefore = function(node) {
    this.next = node;
    this.prev = node.prev;
    this.next.prev = this;
    if (this.prev)
        this.prev.next = this;
    return this;
}

