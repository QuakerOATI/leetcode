/*
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * @param {TreeNode} root
 * @param {number} key
 * @return {TreeNode}
 */
var deleteNode = function(root, key) {
    // 94.08 %ile runtime
    // 75.00 %ile memory
    if (!root)
        return root;
    let dummy = new TreeNode(null, null, null);
    dummy.left = root;
    let [prev, curr] = [dummy, root];
    while (curr.val !== key && !curr.isLeaf()) {
        if (curr.val < key)
            [curr, prev] = [curr.right, curr];
        else
            [curr, prev] = [curr.left, curr];
    }
    while (curr.val === key && !curr.isLeaf()) {
        if (curr.left != null) {
            let [pred, par] = curr.getPredecessor();
            [curr.val, pred.val] = [pred.val, curr.val];
            [curr, prev] = [pred, par];
        } else if (curr.right != null) {
            let [succ, par] = curr.getSuccessor();
            [curr.val, succ.val] = [succ.val, curr.val];
            [curr, prev] = [succ, par];
        }
    }            
    if (key === curr.val) {
        // now we can just remove it since it's a leaf
        switch (curr) {
            case prev.left:
                prev.left = null;
                break;
            case prev.right:
                prev.right = null;
                break;
            default:
                break;
        }
    }
    return dummy.left;
};

TreeNode.prototype.isLeaf = function() {
    return this.left == null && this.right == null;
}

TreeNode.prototype.getSuccessor = function() {
    let curr = this.right;
    let par = this;
    if (!curr) return [curr, par];
    while (curr?.left != null) {
        [curr, par] = [curr.left, curr];
    }
    return [curr, par];
}

TreeNode.prototype.getPredecessor = function() {
    let curr = this.left;
    let par = this;
    if (!curr) return [curr, par];
    while (curr?.right != null) {
        [curr, par] = [curr.right, curr];
    }
    return [curr, par];
}
