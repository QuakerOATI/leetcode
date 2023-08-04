/**
 * @param {number[]} scores
 * @param {number[][]} edges
 * @return {number}
 */
var maximumScore = function(scores, edges) {
    let paths = Object.fromEntries(scores.map((s, i) => [i, {score: s}]));
    let graph = Array.from({length: scores.length}, () => []);
    let seen = [];
    for (let [a, b] of edges) {
        graph[a].push(b);
        graph[b].push(a);
    }
    var bfs = function(n) {
        let adj = graph[n];
        for (let m of adj.filter(seen.indexOf(m) === -1)) {
            seen.push(m);
};

var table = (arr, sep) => arr.map((x, i) => `${i}: [${x}]`).join(sep);

var maximumScoreDuality = function(scores, edges) {
    console.log(`Scores:\n\t[${table(scores, "\n\t ")}]`);
    console.log(`Graph:\n\t[${table(edges, "\n\t ")}]`);
    var bestEdges = Array.from({length: scores.length}, () => []);
    var addEdge = function(edge) {
        let [a, b] = edge;
        bestEdges[a] = [...bestEdges[a], b].sort((x, y) => scores[x] - scores[y]).slice(-3);
    }
    var bestPathSum = -1;
    var pickOneFromEach = (arrs) => arrs.some(a => !a.length) ? [] :
        arrs.map((a, i) => 
            [a.at(-1), arrs[(i+1)%arrs.length].findLast(x => x !== a.at(-1))].filter(x => x != null)
        ).filter(x => x.length === 2);
        
    edges.forEach(e => {addEdge(e); addEdge(e.reverse());});
//    console.log(`Best edges:\n\t[${table(bestEdges, "\n\t ")}]`);

    for (let e of edges) {
//        console.log(`Considering paths with middle edge [${e}]`);
//        console.log(`   best edges for ${e[0]}: [${bestEdges[e[0]]}] --> [${bestEdges[e[0]].map(e => scores[e])}]`);
//        console.log(`   best edges for ${e[1]}: [${bestEdges[e[1]]}] --> [${bestEdges[e[1]].map(e => scores[e])}]`);
//        console.log(`   best edges (filtered): ${[e.map(n => bestEdges[n].filter(x => e.indexOf(x) === -1))]}`);
        let p = pickOneFromEach(e.map(n => bestEdges[n].filter(x => e.indexOf(x) === -1)));
//        console.log(`   pick one output: ${p}`);
//        console.log(`   best pick sums: [${p.map(a => a.reduce((S, x) => S + scores[x], 0))}]`);
        bestPathSum = Math.max(bestPathSum, 
            ...p.map(a => a.concat(e).reduce((S, x) => S + scores[x], 0))
        );
    }
    return bestPathSum;        
}

var maximumScoreDFS = function(scores, edges) {
    // TLE
    let memo = {};
    var getMemo = function(start, ...visited) {
        let key = `${start}:${visited.sort()}`;
        return memo[key];
    }
    var putMemo = function(ans, start, ...visited) {
        let key = `${start}:${visited.sort()}`;
        memo[key] = ans;
    }
    let nodes = Array.from({length: scores.length}, () => []);
    for (let [a, b] of edges) {
        nodes[a].push(b);
        nodes[b].push(a);
    }
    var dfs = function(start, ...visited) {
        if (visited.indexOf(start) >= 0 || visited.length > 3)
            return -Infinity;
        else if (visited.length === 3)
            return scores[start];
        else if (ans = getMemo(start, ...visited))
            return ans;
        visited.push(start);
        let best = -Infinity;
        for (let n of nodes[start]) {
            best = Math.max(best, scores[start] + dfs(n, ...visited));
        }
        putMemo(best, visited.pop(), ...visited);
        return best;
    }
    let max = -Infinity;
    for (let n=0; n<scores.length; ++n) {
        max = Math.max(max, dfs(n));
    }
    return isFinite(max) ? max : -1;
};
