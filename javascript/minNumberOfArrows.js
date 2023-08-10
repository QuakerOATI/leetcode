/*
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
*/

/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    // 44.99 %ile runtime
    // 5.13 %ile memory
    let ct = 0;
    let [ci, cf] = [-Infinity, -Infinity];
    for (let [xi, xf] of points.sort((p1, p2) => p1[0] - p2[0])) {
        ci = xi;
        cf = Math.min(cf, xf);
        if (ci > cf) {
            ct++;
            cf = xf;
        }
    }
    return ct;
};
