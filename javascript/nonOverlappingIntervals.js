/*
 Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
 */

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    // single-processor scheduling problem?
    // 96.22 %ile runtime
    // 30.19 %ile memory
    intervals.sort((i1, i2) => i1[1] - i2[1]);
    let start = -Infinity;
    let ct = 0;
    for (let I of intervals) {
        if (I[0] < start)
            ct++;
        else
            start = I[1];
    }
    return ct;
};
