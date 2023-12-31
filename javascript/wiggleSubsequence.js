/*
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(nums) {
    // This DP solution works, but is asymptotically suboptimal
    // Best is O(n)
    // 5.45 %ile runtime
    // 5.45 %ile memory
    let best = 1;
    var dp = Array.from({length: nums.length}, () => Object.fromEntries([[1, 0], [-1, 0]]));
    dp[0][1] = dp[0][-1] = 1;
    for (let i=1; i<nums.length; ++i) {
        dp[i][1] = 1 + Math.max(
            ...dp.slice(0, i).filter((x, j) => nums[j] < nums[i]).map(x => x[-1]));
        dp[i][-1] = 1 + Math.max(
            ...dp.slice(0, i).filter((x, j) => nums[j] > nums[i]).map(x => x[1]));
        best = Math.max(best, dp[i][1], dp[i][-1]);
    }
    return best;
};
