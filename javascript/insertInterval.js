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
    if (l === 0) {
        newInterval[1] = Math.max(newInterval[1], intervals[Math.ceil((r+1)/2)][1]);

    if (l === r) {
        if (l % 2 === 0)
            return intervals.slice(0, l).concat([newInterval]).concat(intervals.slice(l));
        else
            return intervals;
    }


    let replaceLeft = (l%2 === 1 || l === 0);
    let replaceRight = (r%2 === 1 || r >= 2*intervals.length);
    [l, r] = [Math.floor((l+1)/2), Math.ceil((r+1)/2)];
    if (l === r) {
        if (replaceLeft || replaceRight)
            // Case 1: newInterval is contained in one of the old ones
            return intervals;
        else
            // Case 2: newInterval is disjoint from all of the old ones
            return intervals.slice(0, 
    if (replaceLeft && replaceRight) {
        [l, r] = [l === 0 ? 0 : (l-1)/2, Math.floor(r/2)];
        newInterval = [Math.min(intervals[l][0], newInterval[0]),
            Math.max(intervals[r][1], newInterval[1])];
    } else if (replaceLeft) {
        [l, r] = [l === 0 ? 0 : (l-1)/2), r/2];
        newInterval = [Math.min(intervals[l][0], newInterval[0]), newInterval[1]];
    
    intervals = intervals.slice(0, l).concat([newInterval]).concat(intervals.slice(r+1));
    
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
    let [l, m, r] = [0, Math.floor(nums.length/2), math.length-1];
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
    let [l, m, r] = [0, Math.floor(nums.length/2), math.length-1];
    while (r-l > 1) {
        [l, m, r] = x < nums[m] ? [l, Math.floor((m+r)/2), m] : [m, Math.floor((l+m)/2), r];
    }
    if (x < nums[r])
        return r;
    else
        return r+1;
}
