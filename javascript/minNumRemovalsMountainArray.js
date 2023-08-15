/*
You may recall that an array nums is a mountain array if and only if:

nums.length >= 3
There exists some index i (0-indexed) with 0 < i < nums.length - 1 such that:
nums[0] < nums[1] < ... < nums[i - 1] < nums[i]
nums[i] > nums[i + 1] > ... > nums[nums.length - 1]
Given an integer array nums¿?¿?¿?, return the minimum number of elements to remove to make nums¿?¿?¿? a mountain array.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumMountainRemovals = function(nums) {
    if (nums.length < 4) {
        return 0;
    }
    let best = Infinity;
    let sortedLeft = [[0, 0]], sortedRight = [[0, 0]];
    for (let i = 1; i < nums.length-1; ++i) {
        let il = bisectLeft(sortedLeft, [i, 0], (x, y) => nums[x[0]] - nums[y[0]]);
        sortedLeft.push([i, i - il]);
        let ir = bisectLeft(sortedRight, [i, 0], 
            (x, y) => nums[nums.length-x[0]-1] - nums[nums.length-y[0]-1]);
        sortedRight.push([i, i - ir]);
        if (i >= nums.length/2) {
            best = Math.min(best, sortedLeft[i][1] + sortedRight[nums.length-i-1][1],
                sortedLeft[nums.length-i-1][1] + sortedRight[i][1]);
        }
    }
    return best;
};

var bisectLeft = function(nums, x, cmp) {
    let l = 0, r = nums.length - 1;
    while (r > l) {
        let m = Math.floor((l+r)/2);
        if (cmp(x, nums[m]) <= 0)
            r = m;
        else
            l = m + 1;
    }
    return l;
}
