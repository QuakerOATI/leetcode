/*
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
*/

/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes = function(graph) {
    // 16.92 %ile runtime
    // 7.30 %ile memory
    // Interestingly, a recursive solution works fine here, see near-optimal solution below
    var safe = [];

    var sgraph = (g) => `[${g.map(a => "[" + a.join(",") + "]")}]`;

    var markNode = function(n, mark) {
        graph[n].unshift(isFinite(mark) ? ~mark : mark);
    }
    var hasMark = (n, mark) => graph[n][0] === (isFinite(mark) ? ~mark : mark);
    var removeMark = (n) => graph[n].length && isFinite(graph[n][0]) ? ~graph[n].shift() : graph[n].shift();
    var dfs = function(idx) {
        if (graph[idx] && graph[idx][0] === Infinity)
            return true;
        else if (graph[idx] && graph[idx][0] < 0)
            return false;
        console.log(`-------------BEGIN-------------`);
        console.log(`Beginning DFS at node ${idx}\n\tgraph = ${sgraph(graph)}`);
        let prev = -Infinity;
        let curr = idx;
        while (true) {
            console.log(`==============DFS iteration state:==============\n\tcurr = ${curr}\n\tprev = ${prev}\n\tgraph = ${sgraph(graph)}`);
            if (curr < 0 || curr >= graph.length) {
                // this should never be triggered
                console.log(`WARNING: Abnormal state reached in DFS: curr === ${curr}\n`);
                return false;
            }
            let adj = graph[curr];
            if (adj.length && adj[0] < 0) {
                // node is known to be unsafe
                // or, node has already been visited: either a cycle or backtracking
                if (prev === Infinity) {
                    // Revisiting node via backlink
                    console.log(`   Revisiting node ${curr} (parent ${prev})`);
                } else {
                    // cycle found: mark this and all prev nodes as unsafe
                    // this can be accomplished simply by leaving the marks in place
                    // the exception for prev is so that we can follow the "breadcrumbs" without triggering the stop condition
                    console.log(`Cycle found at node ${curr}`);
                    console.log(`----------TERMINATE-----------\n`);
                    return false;
                }
            } else {
                markNode(curr, prev);
            }
            if (adj.at(-1) >= 0 && isFinite(adj.at(-1))) {
                // visiting node for the first time
                // the finiteness check rules out known-to-be-safe nodes
                console.log(`Visiting node ${curr} for the first time from parent ${prev}`);
                [curr, prev] = [adj.pop(), curr];
            } else {
                // terminate search and follow the backlinks
                console.log(`End of search reached at node ${curr}\n\tFollowing backlink to ${~adj[0]}...`);
                if (adj.length && adj[0] === -Infinity) {
                    // exhausted search root; mark safe and return true
                    console.log(`Reached end of DFS at root node ${curr}.  Marking "safe"`);
                    adj[0] = Infinity
                    return true;
                }

                [curr, prev] = [removeMark(curr), curr];
                // use Infinity as a sentinel to indicate "safe" nodes
                markNode(prev, Infinity);
                prev = Infinity;
            }
            console.log(sgraph(graph));
            console.log(`==============End of iteration=============\n`);
        }
    }
    for (let i=0; i<graph.length; ++i) {
        if (graph[i][0] >= 0 && isFinite(graph[i][0]))
            dfs(i);
        if (!graph[i].length || graph[i][0] === Infinity)
            safe.push(i);
    }
    return safe;
};

// Near-optimal solution using recursion
function eventualSafeNodesOptimal(graph) {
    const n = graph.length;

    const isSafe = new Array(n);
    const visited = new Array(n);

    for (let i = 0; i < n; i++) traverse(i);

    function traverse(node) {
        if (isSafe[node] !== undefined) return isSafe[node];

        if (visited[node]) {
            isSafe[node] = false;
            return false;
        }

        visited[node] = true;

        for (const edge of graph[node]) {
            if (!traverse(edge)) {
                isSafe[node] = false;
                break;
            }
        }

        isSafe[node] = isSafe[node] ?? true;

        return isSafe[node];
    }

    const result = [];

    for (let i = 0; i < n; i++) {
        if (isSafe[i]) result.push(i);
    }

    return result;
};

var binarySearch = (arr, n) => {
    if (!arr.length || n < arr[0] || n > arr.at(-1))
        return false;
    if (arr.length === 1)
        return n === arr[0];
    else {
        let [l, r] = [0, arr.length-1];
        while (l < r) {
            let m = Math.floor((l+r)/2);
            if (arr[m] < n)
                l = m + 1;
            else
                r = m;
        }
        return n === arr[l];
    }
};
