/*
Given two strings s and t of lengths m and n respectively, return the minimum window substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

BONUS: Find an algorithm that runs in O(m + n).
*/

/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    // 90.34 %ile runtime
    // 85.52 %ile memory
    let ct = {};
    for (let c of t) {
        ct[c] = ct[c] ?? 0;
        ++ct[c];
    }
    let rem = t.length, l = 0, best = [0, Infinity];
    for (let r = 0; r < s.length; ++r) {
        if (ct.hasOwnProperty(s[r])) {
            --ct[s[r]];
            if (ct[s[r]] >= 0)
                --rem;
        }
        if (rem <= 0) {
            for (; !ct.hasOwnProperty(s[l]) || ct[s[l]] < 0; ++l) {
                if (ct.hasOwnProperty(s[l])
                    ++ct[s[l]];
            }
            if (r - l + 1 < best[1] - best[0])
                best = [l, r+1];
        }
    }
    return isFinite(best[1]) ? s.slice(...best) : "";
};
