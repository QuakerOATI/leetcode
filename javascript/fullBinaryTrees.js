// Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.
// 
// Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
// 
// A full binary tree is a binary tree where each node has exactly 0 or 2 children.

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number} n
 * @return {TreeNode[]}
 */

// Accepted, and apparently close to optimal.
// This might be because I "cheated" by shadowing TreeNode, however (the judge provides a **class**, so TreeNodes in other solutions are instantiated using `new`).
var TreeNode = function(val, left, right) {
    return {
        val, left, right,/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    
};
        toString: function() {
            let stack = [this];
            let ret = [];
            while (stack.length) {
                let curr = stack.pop();
                if (curr) {
                    ret.push(curr.val);
                    stack.push(curr.left);
                    stack.push(curr.right);
                } else {
                    ret.push(curr);
                }
            }
            return "[" + ret.map(x => (x===null ? "null" : x.toString())).join(",") + "]";
        }
    };
}
var allPossibleFBT = function(n) {
    var trees = {
        1: [TreeNode(0, null, null)],
        2: [],
        3: [TreeNode(0, TreeNode(0, null, null), TreeNode(0, null, null))]
    };
    var allPossibleFBTHelper = function(k) {
        if (!trees.hasOwnProperty(k)) {
            trees[k] = [];
            for (let i=1; i<k-1; ++i) {
                allPossibleFBTHelper(k-i-1).forEach(t1 => {
                    allPossibleFBTHelper(i).forEach(t2 => {
                        trees[k].push(TreeNode(0, t1, t2));
                    });
                });
            }
        }
        return trees[k];
    }
    return allPossibleFBTHelper(n);
};
