/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */

// 83.04 %ile runtime, 39.82 %ile memory
// Memory usage can be reduced by using regular arrays instead of Maps an Sets
// This is justified by looking at the maximum allowed values of numCourses and prerequisites.length
var canFinish = function(numCourses, prerequisites) {
    // topological sort
    let succ = Object.fromEntries([...Array(numCourses).keys()].map(x => [x, []]));
    let numPrereqs = Object.fromEntries([...Array(numCourses).keys()].map(x => [x, 0]));
    let next = new Set(Array(numCourses).keys());
    for (let [c, p] of prerequisites) {
        succ[p].push(c);
        next.delete(c);
        if (!next.size)
            return false;
        numPrereqs[c]++;
    }
    next = [...next];
    while (next.length) {
        let p = next.pop();
        //console.log(`${p}: ${succ[p]}`);
        for (let c of succ[p]) {
            if (--numPrereqs[c] === 0)
                next.push(c);
        }
        numCourses--;
    }
    return numCourses === 0;
};
