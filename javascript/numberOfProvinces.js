/*
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
/*

/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(isConnected) {
    // 67.56 %ile runtime
    // 33.21 %ile memory
    // This can be improved somewhat by using DFS to completely eliminate each connected component on discovery.
    var n = isConnected.length;
    var adjList = Array(n).fill(-1);
    var getRoot = (idx) => {
        for (; adjList[idx] >= 0; idx = adjList[idx]);
        return idx;
    };
    let numComps = n;
    for (let i=0; i<n-1; ++i) {
        for (let j=i+1; j<n; ++j) {
            if (isConnected[i][j]) {
                let [r1, r2] = [i, j].map(getRoot);
                if (r1 !== r2) {
                    adjList[r1] = r2;
                    numComps--;
                }
            }
        }
    }
    return numComps;
};

