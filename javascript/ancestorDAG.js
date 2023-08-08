/*
You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges.
*/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[][]}
 */
var getAncestors = function(n, edges) {
    // 86.36 %ile runtime
    // 100.00 %ile memory
    // A routine problem, but instructive in the dangers of overzealous optimization.
    var pred = Array.from({length: n}, () => []);
    var last = new Set(Array(n).keys());
    for (let [a, b] of edges.sort((e1, e2) => e1[0] - e2[0])) {
        pred[b].push(a);
        last.delete(a);
    }
    var traversed = new Set();
    var dfs = function(node) {
        if (traversed.has(node))
            return;
        let parents = [...pred[node]];
        parents.forEach(p => dfs(p));
        pred[node] = mergeSortedUnique(parents, ...parents.map(x => pred[x]));
        traversed.add(node);
    };
    last.forEach(l => dfs(l));
    return pred;
}

var mergeSortedUnique = function(...arrs) {
    let js = Array(arrs.length).fill(0);
    let ret = [];
    let done = false;
    while (!done) {
        done = true;
        let m = Infinity, j = -1;
        for (let i=0; i<js.length; ++i) {
            if (js[i] < arrs[i].length) {
                done = false;
                let elem = arrs[i][js[i]];
                if (elem === ret.at(-1) || elem === m) {
                    js[i]++;
                    continue;
                } else if (elem < m) {
                    m = elem;
                    j = i;
                }
            }
        }
        if (!done) {
            ret.push(m);
            js[j]++;
        }
    }
    return ret;
}

