/*
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.
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
 * @param {number} startValue
 * @param {number} destValue
 * @return {string}
 */
var getDirections = function(root, startValue, destValue) {
    // 5.5 %ile runtime
    // 16.9 %ile memory
    let parents = {};
    let stack = [root];
    while ((!parents.hasOwnProperty(startValue) || !parents.hasOwnProperty(destValue)) && stack.length) {
        let curr = stack.pop();
        [curr.left, curr.right].forEach((x, i) => {
            if (x == null) return;
            parents[x.val] = [curr.val, i];
            stack.push(x);
        });
    }
    let path = [startValue], tail = [destValue];
    let up = "", down = "";
    let j, lr;
    while (startValue != null || destValue != null) {
        startValue = parents[startValue] && parents[startValue][0];
        [destValue, lr] = parents[destValue];
        if (startValue != null) {
            console.log(`1st branch: visiting ${startValue}`);
            if (startValue !== path[0]) {
                up += "U";
                path.push(startValue)
            }
            j = tail.indexOf(startValue);
            if (j !== -1) {
                console.log(`1st branch: up = ${up}, down = ${down}`);
                return up + down.slice(j);
            }
        }
        if (destValue != null) {
            console.log(`2nd branch: visiting ${destValue}`);
            down = (lr ? "R" : "L") + down;
            if (lr && destValue !== tail.at(-1)) {
                tail.unshift(destValue); 
            }
            j = path.indexOf(destValue);
            if (j !== -1) {
                console.log(`2nd branch: up = ${up}, down = ${down}`);
                return up.slice(0, j) + down;
            }
        }
    }
    console.log(`path = [${path}]\ntail = [${tail}]`);
};
