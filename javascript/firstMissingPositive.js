// Given an unsorted integer array nums, return the smallest missing positive integer.
//
// You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function (nums) {
    let digits = Array(32).fill(0);
    let sums = Array(32).fill(0);
    let masks = [...Array(32).keys()].map(i => (1 << (i+1)) - 1);
    let [m, M] = [Infinity, 0];
    for (let num of nums.filter(x => x > 0)) {
        [m, M] = [Math.min(m, num), Math.max(M, num)];
        masks.forEach((m, i) => {
            sums[i] += (m & num); 
            digits[i] += (1 + (m>>1)) & num;
        });
    }
    if (m > 1)
        return 1;
    


};
