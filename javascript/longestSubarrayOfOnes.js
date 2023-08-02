// Given a binary array nums, you should delete one element from it.
//
// Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    // This works but is very suboptimal
    // 12.05 %ile runtime, 5.15 %ile memory
    if (nums.length < 2)
        return 0;
    let dp = [];
    let best = nums[0];
    dp.push([nums[0], 0]);
    for (let i=1; i<nums.length; ++i) {
        let arr;
        if (nums[i])
            arr = [1 + dp[i-1][0], 1 + Math.max(dp[i-1][1], i > 1 ? dp[i-2][0] : 0)];
        else
            arr = [0, dp[i-1][0]];
        best = Math.max(best, arr[1]); 
        dp.push(arr);
    }
    return best;
};
