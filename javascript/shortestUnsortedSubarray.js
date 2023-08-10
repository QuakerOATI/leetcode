/*
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findUnsortedSubarray = function(nums) {
    let l = 0, r = nums.length - 1;
    for (; l<nums.length-1 && nums[l]<=nums[l+1]; ++l);
    if (l >= nums.length)
        return 0;
    for (; r>=0 && nums[r] >= nums[r-1]; --r);
    if (l >= r)
        return 0;

    let t = Math.min(...nums.slice(l+1));
    let a = 0, b = l;
    while (a < b) {
        let m = Math.floor((a+b)/2);
        if (nums[m] >= t) b = m-1;
        else a = m + 1;
    }
    console.log(`l = ${l}, r = ${r}\nt = ${t}, a = ${a}, b = ${b}`);
    return r - a;
};

var findUnsortedSubarrayShort = function(nums) {
    // Works, but inferior (by constant factors)
    // 17.39 %ile runtime
    // 5.22 %ile memory
    let ord = [...nums.keys()].sort((k1, k2) => nums[k1] - nums[k2]);
    let l, r;
    for (l = 0; l < nums.length && ord[l] === l; ++l);
    if (l >= nums.length)
        return 0;
    for (r = nums.length - 1; r >= 0 && ord[r] === r; --r);
    return r - l + 1;
}

var findUnsortedSubarrayOptimal = function(nums) {
    // 93.91 %ile runtime
    // 83.48 %ile memory
    // The best method relies on a double-counting argument:
    // * scan the array from both sides
    // * "count" all elements from the left up to the last non-sequential element
    // * do the same from the right
    // * add the counts
    // * the elements that are double-counted are precisely the ones that need to be sorted
    let l = -1, r = -1;             // handles the case nums.length === 1
    let M = nums[0], m = nums[nums.length - 1]; 
    for (let i = 1; i < nums.length; ++i) {
        nums[i] < M ? r = i : M = nums[i];
        nums[nums.length - i - 1] > m ? l = i : m = nums[nums.length - i - 1];
    }
    return Math.max(0, r + l - nums.length + 2);    // l + 1 --> num elems in right group
}


