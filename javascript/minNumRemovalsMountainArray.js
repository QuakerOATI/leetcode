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
    let sortedLeft = [{i: 0, ht: 0}];
    let sortedRight = [{i: nums.length-1, ht: 0}];
    let hts = Array(nums.length).fill(0);
    for (let i = 1; i < nums.length-1; ++i) {
        console.group(`ITERATION: ${i}`);
        let left = {i}, right = {i: nums.length-i-1};
        let jl = bisectLeft(sortedLeft, left, (x, y) => nums[x.i] - nums[y.i]);
        let jr = bisectLeft(sortedRight, right, (x, y) => nums[x.i] - nums[y.i]);
        left.ht = jl ? sortedLeft[jl-1].ht + 1 : 0;
        right.ht = jr ? sortedRight[jr-1].ht + 1 : 0;
        hts[i] += left.ht;
        hts[right.i] += right.ht;
        sortedLeft.splice(jl, 0, left);
        sortedRight.splice(jr, 0, right);
        console.log(`nums[i] = ${nums[i]}, nums[ir] = ${nums[right.i]}`);
        console.log(`jl = ${jl}, jr = ${jr}`);
        console.table(sortedLeft.map(x => `{i: ${x.i}, ht: ${x.ht}, nums[i]: ${nums[x.i]}}`));
        console.table(sortedRight.map(x => `{i: ${x.i}, ht: ${x.ht}, nums[i]: ${nums[x.i]}}`));
        console.table(hts);
        console.groupEnd();
    }
    console.table(hts);
    return nums.length - Math.max(...hts) - 2;
};

var bisectLeft = function(nums, x, cmp) {
    if (nums.length === 0)
        return 0;
    else if (nums.length === 1)
        return cmp(x, nums[0]) > 0 ? 1 : 0;
    let l = 0, r = nums.length - 1;
    while (r > l) {
        let m = Math.ceil((l+r)/2);
        if (cmp(x, nums[m]) <= 0)
            r = m;
        else
            l = m + 1;
    }
    return l;
};
