/**
 * @param {number} n
 * @param {number[]} batteries
 * @return {number}
 */
var maxRunTime = function(n, batteries) {
    var stringify = (b) => JSON.stringify([...b].sort());
    var listSubsets = function*(bs, size) {
        if (bs.length < size || size === 0)
            yield [];
        else if (bs.length === size)
            yield bs;
        else {
            for (let k=0; k+size-1<bs.length; ++k) {
                yield* [...listSubsets(bs.slice(k+1), size-1)].map(s => [bs[k], ...s]);
            }
        }
    }
    if (batteries.length === n)
        return Math.min(...batteries);
    batteries.sort();
    let dp = {};
    var backtrack = function(bs) {
        console.log(`Backtracking with bs = ${bs}`);
        let best = 0;
        if (bs.filter(b => b > 0).length < n)
            return 0;
        else if (dp.hasOwnProperty(stringify(bs))) {
            console.log(`Using cached result for ${bs}: best = ${dp[stringify(bs)]}`);
            return dp[stringify(bs)];
        }
        for (let indices of listSubsets([...bs.keys()].filter(j => bs[j]), n)) {
            console.log(`Checking first minute ${indices}...`);
            indices.forEach(i => bs[i]--);
            best = Math.max(1 + backtrack(bs, n), best);
            indices.forEach(i => bs[i]++);
        }
        dp[stringify(bs)] = best;
        return best;
    }
    return Math.min(...batteries) + backtrack(batteries.map(b => b - Math.min(...batteries) + 1)) - 1;
};


    // Constraints:
    // 1. every computer needs a battery at any given minute;
    // 2. no battery can be used more than once on any given minute;
    // 3. the total number of minutes battery i is in use may not exceed batteries[i];
    // 4. in the final state, fewer than n batteries must remain available.
    //
    // Possibilities:
    // p_{ij} := possibility that battery i is in use during minute j
    //
    // Recursive backtracking:
    // assume p_{k,0}
    //
    // Greedy:
    // replace drained batteries with biggest possible
    
    var solveForOneComp = (batteries) => batteries.reduce((S, b) => S + b, 0);
