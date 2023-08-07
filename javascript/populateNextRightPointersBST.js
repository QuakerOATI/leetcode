/*
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
*/

/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function(root) {
    var connectRecursive = function(node, right) {
        if (!node) return;
        node.next = right;
        if (node.left && node.right) {
            connectRecursive(node.left, node.right);
            connectRecursive(node.right, right?.left ?? null);
        }
    }
    connectRecursive(root, null);
    return root;
};

Node.prototype.greatestDescendant = function() {
    let curr = this;
    for (; curr.right; curr = curr.right);
    return curr;
}

Node.prototype.leastDescendant = function() {
    let curr = this;
    for (; curr.left; curr = curr.left);
    return curr;
}

Node.prototype.print = function() {
    for (let curr = this; curr; curr = curr.left) {
        let s = "";
        for (let n = curr; n; n = n.next) {
            s += `  ${n.val}  `;
        }
        console.log(s);
    }
}

