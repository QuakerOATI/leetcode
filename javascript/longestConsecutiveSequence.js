/*
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    // 30.47 %ile runtime
    // 7.38 %ile memory
    let dp = {};
    let best = 0;
    for (let num of nums) {
        console.group(`ITERATION: ${num}`);
        if (!dp.hasOwnProperty(num))
            dp[num] = {start: 1, stop: 1};
        dp[num].stop = 1 + (dp[num-1]?.stop ?? 0);
        dp[num].start = 1 + (dp[num+1]?.start ?? 0);
        if (dp.hasOwnProperty(num+1))
            dp[num+1].stop = Math.max(dp[num].stop + 1, dp[num+1].stop);
        if (dp.hasOwnProperty(num-1))
            dp[num-1].start = Math.max(dp[num].start + 1, dp[num-1].start);
        let total = dp[num].start + dp[num].stop - 1;
        let x = num - dp[num].stop + 1, y = num + dp[num].start - 1;
        dp[x].start = Math.max(dp[x].start, total);
        dp[y].stop = Math.max(dp[y].stop, total);
        best = Math.max(best, total);
        console.log(`best = ${best}`);
        console.table(dp[num], `dp[${num}]`);
        console.groupEnd();
    }
    return best;
};
