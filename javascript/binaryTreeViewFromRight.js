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
 * @return {number[]}
 */

// 68.6 %ile runtime, 59.6 %ile memory
var rightSideView = function (root) {
  if (!root)
    return [];
  let ret = [];
  let q = [root];
  while (q.length) {
    ret.push(q.at(-1).val);
    q = q.map(x => [x.left, x.right].filter(y => y)).flat();
  }
  return ret;
};
