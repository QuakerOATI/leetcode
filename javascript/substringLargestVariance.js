/* 
 * The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. 
 * Note the two characters may or may not be the same.  
 * Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.  
 * (A substring is a contiguous sequence of characters within a string.)
 */

/**
 * @param {string} s
 * @return {number}
 */
var largestVariance = function(s) {
    var maxSubArray = function(arr) {
        console.log(`maxSubArray([${arr}])`);
        let vals = [[0, 0]];
        if (arr[0] > 0) vals[0][0] += arr[0];
        else if (arr[0] < 0) vals[0][1] += Math.abs(arr[0]);
        let max = 0;
        console.log(`   Starting loop with max = ${max}, arr = [${arr}], vals = [${vals}]...`);
        for (let b=1; b<arr.length; ++b) {
            vals.push([...vals[b-1]]);
            if (arr[b] > 0) vals[b][0] += arr[b];
            if (arr[b] < 0) vals[b][1] += Math.abs(arr[b]);
            console.log(`   Calculating max at index ${b}`);
            max = Math.max(max, arr[b][0], arr[b][1]);
        }
        return max;
    }
    let best = 0;
    let alpha = 'abcdefghijklmnopqrstuvwxyz';
    let dp = Array.from({length: s.length}, () => Array(alpha.length).fill(0));
    dp[-1] = Array(alpha.length).fill(0);
    for (let i=0; i<s.length; ++i) {
        for (let j=0; j<alpha.length; ++j) {
            console.log(`Setting dp[${i}][${j}]...`);
            dp[i][j] = dp[i-1][j] + (s[i] === alpha[j] ? 1 : s[i] === alpha[(j+1) % 26] ? -1 : 0);
        }
    }
    for (let l=0; l<s.length-1; ++l) {
        for (let r=l+1; r<s.length; ++r) {
            console.log(`Calculating msa for l = ${l}, r = ${r}...`);
            let msa = maxSubArray(dp[r].map((x, i) => x - dp[l-1][i]));
            best = Math.max(msa, best);
        }
    }
    return best;
};

var largestBinaryVariance = (s, a, b) => 
    Array(s).reduce((t, c) => t + (c === a ? 1 : c === b ? -1 : 0));
