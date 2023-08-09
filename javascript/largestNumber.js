/*
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
*/

/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    // 39.87 %ile runtime (regex?)
    // 99.78 %ile memory
    var radixSort = function(a, b) {
        if (a === b || a.length === 0 || b.length === 0)
            return 0;
        if (b.startsWith(a)) {
            return radixSort(a, b.substr(a.length));
        }
        if (a.startsWith(b)) {
            return -radixSort(b, a.substr(b.length));
        }
        return a < b ? 1 : -1;
    }
    let x = nums.map(x => x.toString()).sort(radixSort).join("").replace(/^0*/, "");
    return x.length ? x : '0';
};
