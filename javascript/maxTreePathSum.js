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
 * @return {number}
 */
var maxRootTerminalPath = root => root ? root.val + Math.max(
  ...[root.left, root.right].filter(x => x).map(maxRootTerminalPath), 0
) : -Infinity;

var maxPathSum = root => {
  if (!root)
    return 0;
  let c = [root.left, root.right].filter(x => x);
  return Math.max(...c.map(maxRootTerminalPath).map(x => x + root.val), ...c.map(maxPathSum), c.map(maxRootTerminalPath).reduce((s, x) => s + x, 0) + root.val);
}

var TreeNode = (val, left = null, right = null) => { return { val, left, right }; };
