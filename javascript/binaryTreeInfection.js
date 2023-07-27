/*You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.
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
 * @param {number} start
 * @return {number}
 */

// 80th %ile runtime, 97th %ile memory
var amountOfTime = function(root, start) {
    var infected = new Set();
    var parents = new Map();
    var stack = [];
    while (root && root.val !== start) {
        [root.left, root.right].filter(n => n).forEach(n => {
            parents.set(n, root);
            stack.push(n);
        });
        root = stack.pop();
    }
    let mins = -1;
    for (let [curr, next] = [[root], []]; curr.length; [curr, next] = [next, []]) {
        curr.forEach(n => {
            infected.add(n.val);
            [n.left, n.right, parents.get(n)]
                .filter(x => x)
                .forEach(x => {
                    if (!infected.has(x.val))
                        next.push(x);
                });
        });
        mins++;
    }
    return mins;
};
