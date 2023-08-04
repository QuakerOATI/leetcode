/**
 * @param {number[]} edges
 * @return {number}
 */
var edgeScore = function(edges) {
    // 100 %ile runtime
    // 84.38 %ile memory
    let scores = Array(edges.length).fill(0);
    for (let i=0; i<edges.length; ++i) {
        scores[edges[i]] += i;
    }
    let max = -Infinity;
    let idx = 0;
    for (let i=0; i<edges.length; ++i) {
        if (scores[i] > max) {
            max = scores[i];
            idx = i;
        }
    }
    return idx;
};
