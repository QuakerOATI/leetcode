/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */

// Very near optimal for JS
var removeNthFromEnd = function(head, n) {
    var sent = new ListNode(null, head);
    let last;
    for (; n--; head=head.next) {}
    for (last=sent; head; [last, head] = [last.next, head.next]) {}
    last.next = last.next?.next;
    return sent.next;    
};
