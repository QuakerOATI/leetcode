// You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
// 
// Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
// 
// Return intervals after the insertion.

/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    if (intervals.length == 0) {
        intervals.push(newInterval);
        return intervals;
    }
        
    let [l, r] = [findInsertionPointLeft, findInsertionPointRight].map(
        (f, i) => f(newInterval[i], intervals.flat())
    );
    let [mergeLeft, mergeRight] = [l, r].map(x => (x === 1 % 2));

    if (l === r) {
        if (mergeLeft)
            intervals = intervals.slice(0, l).concat([newInterval]).concat(intervals.slice(l));
        else
            return intervals;
    } else {
        [l, r] = [l, r].map(x => Math.min(Math.max(Math.floor((x-1)/2), 0), intervals.length-1));
        let [L, R] = [mergeLeft ? l : l+1, mergeRight ? r : r+1];
        intervals = intervals.slice(0, L).concat([[
                Math.min(newInterval[0], intervals[L][0]),
                Math.max(newInterval[1],  R < intervals.length ? intervals[R][1] : -Infinity)
            ]]).concat(intervals.slice(R));
    }
    return intervals;
};

var findInsertionPointLeft = function(x, nums) {
    if (nums.length === 0)
        return 0;
    if (nums.length === 1)
        return (x > nums[0] ? 1 : 0);
    if (nums.length === 2)
        return (x > nums[0] ? (x > nums[1] ? 2 : 1) : 0);
    if (x < nums[0])
        return 0;
    if (x > nums.at(-1))
        return nums.length;
    let [l, m, r] = [0, Math.floor(nums.length/2), Math.length-1];
    while (r-l > 1) {
        [l, m, r] = x > nums[m] ? [m, Math.floor((m+r)/2), r] : [l, Math.floor((l+m)/2), m];
    }
    if (x > nums[l])
        return l+1;
    else
        return l;
}

var findInsertionPointRight = function(x, nums) {
    if (nums.length === 0)
        return 0;
    if (nums.length === 1)
        return (x < nums[0] ? 0 : 1);
    if (nums.length === 2)
        return (x < nums[1] ? (x < nums[0] ? 0 : 1) : 2);
    if (x < nums[0])
        return 0;
    if (x > nums.at(-1))
        return nums.length;
    let [l, m, r] = [0, Math.floor(nums.length/2), Math.length-1];
    while (r-l > 1) {
        [l, m, r] = x < nums[m] ? [l, Math.floor((m+r)/2), m] : [m, Math.floor((l+m)/2), r];
    }
    if (x < nums[r])
        return r;
    else
        return r+1;
}

var printArray = (arr) => (arr ? "[" + arr.join(", ") + "]" : "undefined");
var printMatrix = (mat) => (mat ? printArray(mat.map(printArray)) : "undefined");
var unique = (arr) => arr.reduce((acc, x) => acc.includes(x) ? acc : [...acc, x], []);

var insert = function(intervals, newInterval) {
    var intersects = (int1, int2) => {
        if (!(int1) || !(int2) || int1.length < 2 || int2.length < 2)
            return false;
        let [l1, r1, l2, r2] = [...int1, ...int2];
        return Math.max(r1, r2) - Math.min(l1, l2) <= r1 + r2 - l1 - l2;
    }
    var join = (...arrs) => [Math.min(...arrs.flat()), Math.max(...arrs.flat())];
    if (intervals.length === 0)
        intervals.push(newInterval);
    else {
        let middle = unique(newInterval.map(
            (x, i) => findInsertionPoint(intervals, newInterval, (a, b) => a[i] - b[i])
        ).flat());

        let merged = [newInterval];
        middle.map(i => intervals[i]).forEach(I => {
            if (intersects(I, merged[0]))
                merged[0] = join(merged[0], I);
            else if (I)
                merged.push(I);
        });
        let [L, R] = join(middle);

        console.log(`Middle: ${printArray(middle)}`);
        console.log(`Merged: ${printMatrix(merged)}`);
        console.log(`L = ${L}, R = ${R}`);

        intervals = [
            ...intervals.slice(0, L), 
            ...merged.sort((i1, i2) => i1[0] - i2[0]), 
            ...intervals.slice(R+1)
        ];
    }
    return intervals;
}

var findInsertionPoint = function(arr, elem, cmp) {
    if (arr.length === 0 || cmp(elem, arr[0]) < 0)
        return [0, 0];
    else if (cmp(arr.at(-1), elem) < 0)
        return [arr.length, arr.length];
    let [l, r] = [0, arr.length-1];
    while (r-l > 1) {
        let m = Math.floor((r+l)/2);
        [l, r] = cmp(elem, arr[m]) < 0 ? [l, m] : [m, r];
    }
    return [l, r];
}
