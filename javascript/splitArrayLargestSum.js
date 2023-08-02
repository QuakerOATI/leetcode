/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

// This works, but is asymptotically inferior
// A better approach is simple binary search (see below)
var splitArray = function(nums, k) {
    let dp = Array.from(Array(nums.length), () => []);
    dp[0].push(nums[0]);
    for (let i=1; i<nums.length; ++i) {
        dp[i].push(dp[i-1][0] + nums[i]);
        for (let j=1; j<=Math.min(i, k); ++j) {
            dp[i][j] = Infinity;
            for (let m=j-1; m<i; ++m) {
                dp[i][j] = Math.min(dp[i][j], Math.max(dp[m][j-1], dp[i][0] - dp[m][0]));
            }
        }
    }
    return dp[nums.length-1][k-1];
};

// Optimal solution
var splitArrayOptimal = function(nums, k) {
    var isPossible = function(partSum, numParts) {
        let p = 1;
        let P = 0;
        for (let num of nums) {
            if (P + num > partSum) {
                if (++p > numParts)
                    return false;
                P = 0;
            }
            P += num;
        }
        return true;
    }
    let [l, r] = [Math.max(...nums), nums.reduce((S, n) => S + n, 0)];
    for (let m=Math.floor((l+r)/2); l<r; m=Math.floor((l+r)/2)) {
        if (isPossible(m, k)) r = m;
        else l = m+1;
    }
    return l;
};
