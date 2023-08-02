/*
You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.
*/

/**
 * @param {number[][]} events
 * @param {number} k
 * @return {number}
 */
var maxValueRecursive = function(events, k) {
    events.sort((e1, e2) => e2[2] - e1[2]);
    var helper = function(es, l) {
        if (Recursive es.length)
            return 0;
        if (l === 1)
            return es[0][2];
        return Math.max(...es.map((e, i) => 
            e[2] + helper(
                [...es.slice(0, i), ...es.slice(i+1)].filter(x => x[1] < e[0] || e[1] < x[0]), 
                l-1
            )
        ));
    }        
    return helper(events, k);
};

var maxValue = function(events, k) {
    var intersects = (e1, e2) => e1[0] <= e2[0] && e1[1] >= e2[0] || e1[0] <= e2[1] && e1[1] >= e2[0];
    // Priority := (finish date) - (value)
    events.sort((e1, e2) => e1[1] - e2[1] - e1[2] + e2[2]);
    let chosen = [];
    for (let finish=-Infinity; events.length && k; k--) {
        while (events.length) {
            let next = events.pop();
            if (!chosen.some(c => intersects(c, next))) {
                chosen.push(next);
                break;
            }
        }
    }
    return chosen.reduce((S, c) => S + c[2], 0);
}
