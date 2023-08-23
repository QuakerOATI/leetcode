/*
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    if (nums.length === 0)
        return 0;
    let best = 1;
    let dp = [];
    for (let i = 0; i < nums.length; ++i) {
        let j = bisect_left(dp, nums[i], (n, p) => n - p);
        if (j >= i || nums[i] !== dp[j]) {
            dp.splice(j, 0, nums[i]);
        }
        best = Math.max(best, j + 1);
    }
    return best;
};

var bisect_left = function(vals, n, cmp) {
    if (vals.length === 0)
        return 0;
    else if (cmp(n, vals[vals.length-1]) > 0)
        return vals.length;
    else if (cmp(n, vals[0]) < 0)
        return 0;
    let l = 0, r = vals.length - 1;
    while (l < r) {
        let m = Math.floor((l + r)/2);
        if (cmp(n, vals[m]) > 0)
            l = m + 1;
        else
            r = m;
    }
    return l;
}

