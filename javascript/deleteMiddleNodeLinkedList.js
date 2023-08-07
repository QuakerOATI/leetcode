/*
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the �n / 2�th node from the start using 0-based indexing, where �x� denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    if (!head?.next)
        return null;
    var dummy = new ListNode(null, head);
    var middle = dummy;
    for (; head?.next; [middle, head] = [middle.next ?? middle, head.next?.next]);
    middle.next = middle.next?.next;
    return dummy.next;
};
