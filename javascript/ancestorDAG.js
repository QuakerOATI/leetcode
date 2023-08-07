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
    // Choose node with no successors
    // proof that there is such a node: if not, either there's a cycle or an infinite path
    // Use DFS to get a list of its ancestors
    // Reverse: start at a node with no predecessors
    let cmp = (x, y) => x - y;
    let stack = [];
    var pred = Array.from({length: n}, () => []);
    var adj = Array.from({length: n}, () => []);
    for (let [a, b] of edges) {
        pred[b].push(a);
        adj[a].push(b);
    }
    for (let i=0; i<pred.length; ++i) {
        if (pred[i].length === 0) {
            preorderDfs(i, x => adj[x], x => {pred[
        }
};

var preorderBfs = function

var preorderDfs = function*(node, getNext) {
    if (!node)
        return;
    callback(
    yield node;
    yield* getNext(node).map(x => preorderDfs(x, getNext));
}

var upheap = function(arr, cmp, rootPos=0, heapEnd=-1) {
    if (heapEnd < 0)
        heapEnd -= arr.length*Math.floor(heapEnd/arr.length);
    let pos = heapEnd;
    let p;
    for (p = getParent(arr, pos, rootPos);
        p >= rootPos && cmp(arr[p], arr[pos]) > 0; 
        [pos, p] = [p, getParent(arr, pos, rootPos)]) 
    {
        swap(arr, pos, p);
    }
    return p;
}

var downheap = function(arr, pos, cmp, rootPos=0, heapEnd=-1) {
    if (heapEnd < 0)
        heapEnd -= arr.length*Math.floor(heapEnd/arr.length);
    for (let c = getMinChild(arr, pos, cmp, rootPos, heapEnd); 
        rootPos <= c && c <= heapEnd && arr[c] && cmp(arr[pos], arr[c]) > 0; 
        [pos, c] = [c, getMinChild(arr, c, cmp, rootPos, heapEnd)]) 
    {
        swap(arr, pos, c);
    }
}

var getParent = function(arr, pos, rootPos=0) {
    return Math.floor((pos - rootPos - 1)/2);
}

var getMinChild = function(arr, pos, cmp, rootPos=0, heapEnd=-1) {
    if (heapEnd < 0)
        heapEnd -= arr.length*Math.floor(heapEnd/arr.length);
    return [rootPos + 2*(pos-rootPos)+1, rootPos + 2*(pos-rootPos)+2]
                            .filter(x => x >= rootPos && x <= heapEnd && arr[x])
                            .sort((x, y) => cmp(arr[x], arr[y])).shift();
}

var heappop = function(arr, cmp, rootPos=0, heapEnd=-1) {
    if (arr.length < 2)
        return arr.pop();
    if (heapEnd < 0)
        heapEnd -= arr.length*Math.floor(heapEnd/arr.length);
    console.log(rootPos, heapEnd);
    var tail = arr.slice(heapEnd+1);
    console.log(`tail = [${tail}]`);
    arr = arr.slice(0, heapEnd+1);
    swap(arr, rootPos, heapEnd);
    let ret = arr.pop();
    console.log(`arr (pre-concat) = [${arr}]`);
    downheap(arr, cmp, rootPos);
    arr = arr.concat(tail);
    console.log(`arr (post-concat) = [${arr}]`);
    return ret;
}

var heappush = function(arr, elem, cmp, rootPos=0, heapEnd=-1) {
    if (arr.length < 2) {
        arr.push(elem);
        arr.sort(cmp);
        return;
    }
    if (heapEnd < 0)
        heapEnd -= arr.length*Math.floor(heapEnd/arr.length);
    var tail = arr.slice(heapEnd+1);
    arr = arr.slice(0, heapEnd+1);
    arr.push(elem);
    let pos = upheap(arr, cmp, rootPos);
    downheap(arr, pos, cmp, rootPos);
    arr = arr.concat(tail);
}

var unheap = function(arr, cmp, rootPos=0, heapEnd=-1) {
    if (heapEnd < 0)
        heapEnd -= arr.length*Math.floor(heapEnd/arr.length);
    for (let last=heapEnd; last > rootPos; --last) {
        swap(arr, rootPos, last);
        downheap(arr, rootPos, cmp, rootPos, last-1);
    }
}

var swap = function(arr, i, j) {
    [arr[i], arr[j]] = [arr[j], arr[i]];
}

/*
 * https://michaelha-d.dev.oati.local:8080/ui/microgrid/resources/configurations/Resources
 */
