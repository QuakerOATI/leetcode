/*
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
*/

/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var minimumDeleteSum = function(s1, s2) {
    let codePoints = (s) => s.split('').map(c => c.codePointAt());
    let sum = (arr) => arr.reduce((S, x) => S + x, 0);
    if (s1.length === 0)
        return sum(codePoints(s2));
    else if (s2.length === 0)
        return sum(codePoints(s1));
    let A1 = codePoints(s1), A2 = codePoints(s2);
    let dp = Array.from({length: s1.length}, () => Array(s2.length).fill(0));
    dp[0][0] = A1[0] === A2[0] ? A1[0] : 0;
    let best = 0, S1 = sum(A1), S2 = sum(A2);
    for (let i = 1; i < s1.length; ++i) {
        dp[i][0] = A1[i] === A2[0] ? A2[0] : Math.max(dp[i-1][0], 0);
        best = Math.max(best, dp[i][0]);
    }
    for (let j = 1; j < s2.length; ++j) {
        dp[0][j] = A1[0] === A2[j] ? A1[0] : Math.max(dp[0][j-1], 0);
        best = Math.max(best, dp[0][j]);
    }
    for (let i = 1; i < s1.length; ++i) {
        for (let j = 1; j < s2.length; ++j) {
            dp[i][j] = A1[i] === A2[j] ? dp[i-1][j-1] + A1[i] : Math.max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]);
            best = Math.max(best, dp[i][j]);
        }
    }
    return S1 + S2 - 2*best;
};
