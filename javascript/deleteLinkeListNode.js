/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function(node) {
    let next = node.next;
    while (next?.next) {
        [next.val, node.val] = [node.val, next.val];
        [node, next] = [next, next.next];
    }
    node.val = next.val;
    node.next = null;
};
