/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 */
var Solution = function(head) {
    this.head = head;
    this.values = [];
    for (; head; head = head.next) {
        this.values.push(head.val);
    }
    console.log(`Initialized with values = [${this.values}]`);
};

/**
 * @return {number}
 */
Solution.prototype.getRandom = function() {
    // Instead, it's much more efficient to store the list size and add a dummy node to "circularize" the linked list.
    let i = Math.floor(Math.random()*(this.values.length - 0.0000001));
    console.log(`Returning values[${i}] = ${this.values[i]}`);
    return this.values[i];
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(head)
 * var param_1 = obj.getRandom()
 */
