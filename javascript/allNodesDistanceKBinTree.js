/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} target
 * @param {number} k
 * @return {number[]}
 */

// 80th %ile runtime, 69th %ile memory
var bfs = function(node, depth, found) {
    if (!node) return;
    //console.log(`Starting BFS at node ${node.val}, depth = ${depth}`);
    var queue = [node];
    for (let i=0; i<depth; ++i) {
        queue = queue.map(n => [n?.left, n?.right].filter(x => x)).flat();
    }
    queue.forEach(n => { found.push(n.val); });
}

var distanceK = function(root, target, k) {
    var parents = new Map();
    var stack = [];
    var ret = [];
    while (root && root !== target) {
        [root.left, root.right].forEach(x => {
            if (x) {
                stack.push(x);
                parents.set(x, root);
            }
        });
        root = stack.pop();
    }
    let [skipLeft, skipRight] = [false, false];
    for (; k>0 && root; k--) {
        if (!skipLeft) {
            bfs(root.left, k-1, ret);
        }
        if (!skipRight) {
            bfs(root.right, k-1, ret);
        }
        skipLeft = root === parents.get(root)?.left;
        skipRight = root === parents.get(root)?.right;
        root = parents.get(root);
    }
    if (k === 0 && root) ret.push(root.val);
    return ret;
};
