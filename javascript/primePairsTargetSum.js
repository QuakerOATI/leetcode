/**
 * @param {number} n
 * @return {number[][]}
 */

// It's better to use an array rather than a set, both for runtime and memory
var findPrimePairs = function(n) {
    let comp = new Set([1]);
    for (let i=2; (i-1)*(i-1)<n; ++i) {
        if (!comp.has(i)) {
            for (let k=2; k*i<=n; ++k) {
                comp.add(k*i);
            }
        }
    }
    var ans = [];
    for (let i=1; i<=n/2; ++i) {
        if (!comp.has(i) && !comp.has(n-i))
            ans.push([i, n-i]);
    }
    return ans;
};
