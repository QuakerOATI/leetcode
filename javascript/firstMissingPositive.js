// Given an unsorted integer array nums, return the smallest missing positive integer.
//
// You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    // 95 %ile runtime
    // 73.92 %ile memory
    var swap = function(arr, i, j) {
        if (i === j)
            return;
        [arr[i], arr[j]] = [arr[j], arr[i]];
    };

    for (let i=0; i<nums.length; ++i) {
        while (nums[i] > 0 && nums[i] <= nums.length && nums[i] !== nums[nums[i]-1]) {
            swap(nums, i, nums[i]-1);
        }
    }

    let first = 0;
    while (nums[first++] === first);
    return first;
}

// Useful implementation of partitioning, but too involved for this problem
var firstMissingPositive = function(nums) {
    var swap = function(arr, i, j) {
        if (i === j)
            return;
        [arr[i], arr[j]] = [arr[j], arr[i]];
    };

    var partitionLeft = function(arr, l, r, p) {
        let [ml, Ml] = [p, -Infinity];
        var updateRange = function(n) {
            [ml, Ml] = [Math.min(ml, n), Math.max(Ml, n)];
        }
        console.log(`Partitioning array slice [${arr.slice(l, r+1)}] on pivot ${p}...`);
        for (; arr[r] > p; r--);
        for (; arr[l] <= p; l++) updateRange(arr[l]);
        for (let i=l; i<=r; ++i) {
            if (arr[i] <= p) {
                console.log(`Swapping ${arr[i]} at index ${i} with ${arr[l]} at index ${l}`);
                console.log(`   Incrementing l = ${l} --> ${l+1}...`);
                updateRange(arr[i]);
                swap(arr, i, l++);
                for (; arr[l] <= p; l++) updateRange(arr[l]);
            } else {
                console.log(`Swapping ${arr[i]} at index ${i} with ${arr[r]} at index ${r}`);
                console.log(`   Decrementing r = ${r} --> ${r-1}...`);
                swap(arr, i, r--);
                updateRange(arr[i]);
                for (; arr[r] > p; r--);
            }
            console.log(`State at end of iteration:\n\tl = ${l}\n\tr = ${r}\n\tarr = [${arr}]`);
        }
        return {pivot: r, min: ml, max: Ml};
    }

    var fmpHelper = function(arr, l, r) {
        // not clear what to do from here
        let m = partition(arr, l, r, Math.floor((r - l + 1)/2));
    }

    let l = partition(nums, 0, nums.length-1, 0) + 1;
    console.log(`Array after first partition:\n\t[${nums.slice(0, l)} ; ${nums[l]} ; ${nums.slice(l+1)}]`);
    if (l >= nums.length-1)
        return 1;
    for (let i=0; i<nums.length; ++i) {
        if (nums[i] === next) {
            [nums[i], nums[idx]] = [nums[idx], nums[i]];
            idx++;
            next++;
        }
}

// Half-baked and probably going nowhere
var firstMissingPositiveBinaryBuckets = function (nums) {
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
