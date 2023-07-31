/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

// 100 %ile runtime, 35.32 %ile memory
var maximumJumps = function(nums, target) {
    let dp = [0];
    for (let i=1; i<nums.length; ++i) {
        let J = -1;
        for (let j=0; j<i; ++j) {
            if (dp[j] >= 0 && Math.abs(nums[i] - nums[j]) <= target)
                J = Math.max(J, dp[j] + 1);
        }
        dp.push(J);
    }
    return dp[nums.length - 1];
};
