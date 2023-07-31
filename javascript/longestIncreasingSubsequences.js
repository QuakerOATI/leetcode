/**
 * @param {number[]} nums
 * @return {number}
 */

// 77.4 %ile runtime, 60.89 %ile memory
var findNumberOfLIS = function(nums) {
    var dp = [];
    let best = 1;
    let total = 0;
    for (let i=0; i<nums.length; ++i) {
        let longest = 1;
        let numSeqs = 1;
        for (let j=0; j<i; ++j) {
            if (nums[j] < nums[i]) {
                [subSeq, numSubSeqs] = dp[j];
                if (++subSeq > longest) {
                    numSeqs = numSubSeqs;
                    longest = subSeq;
                } else if (subSeq === longest) {
                    numSeqs += numSubSeqs;
                }
            }
        }
        dp[i] = [longest, numSeqs];
        if (longest > best) {
            total = numSeqs;
            best = longest;
        } else if (longest === best) {
            total += numSeqs;
        }
    }
    return total;
};
