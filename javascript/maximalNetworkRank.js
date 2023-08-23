/*
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
/*

/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var maximalNetworkRank = function(n, roads) {
    if (n < 2)
        return 0;
    else if (n === 2)
        return roads.length ? 1 : 0;
    let degrees = Array(n).fill(0);
    let edges = {};
    for (let [a, b] of roads) {
        ++degrees[a];
        ++degrees[b];
        edges[[Math.min(a, b), Math.max(a, b)]] = 1;
    }
    return Math.max(
        ...Array.from(pairs([...degrees.entries()].sort((x, y) => x[1] - y[1])))
                .map(p => {
                    let [c1, d1] = p[0], [c2, d2] = p[1];
                    return d1 + d2 - (edges[[Math.min(c1, c2), Math.max(c1, c2)]] ?? 0);
                })
    );
};

var pairs = function*(arr) {
    for (let i = 0; i < arr.length - 1; ++i) {
        for (let j = i + 1; j < arr.length; ++j) {
            yield [arr[i], arr[j]];
        }
    }
}
