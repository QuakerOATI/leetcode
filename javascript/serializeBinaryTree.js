// 99.57 %ile runtime, 16.67 %ile memory

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    return JSON.stringify(toArray(root));
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    let arr = JSON.parse(data);    
    return fromArray(arr); 
};

var toArray = function(node) {
    return postOrder(node, (n, l, r) => [n.val, l, r]);
};

var fromArray = function(arr) {
    if (!arr)
        return arr;
    let [val, left, right] = arr;
    var node = new TreeNode(val);
    node.left = fromArray(left);
    node.right = fromArray(right);
    return node;
};

var postOrder = function(node, callback) {
    if (!node)
        return null;
    let left, right;
    if (node.left)
        left = postOrder(node.left, callback);
    if (node.right)
        right = postOrder(node.right, callback);
    return callback(node, left, right);
};
