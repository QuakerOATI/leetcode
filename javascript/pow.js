/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */

// Plagued by TypeErrors due to BigInts
// Simplest is just to return x**n
var myPow = function(x, n) {
    var raisePowerOf2 = function(n, i) {
        try {
            n = BigInt(n);
            for (; i>0; --i) {
                n *= n;
            }
            return n;
        } catch(e) {
            return Infinity;
        }
    }
    if (x === 1)
        return 1;
    else if (x === 0)
        return 0;
    let neg = n < 0;
    let digits = [];
    for (n=Math.abs(n); n; n >>= 1) {
        digits.push(n % 2);
    }
    try {
        return digits.map((d, i) => d ? raisePowerOf2(x, i) : 1n)
                 .reduce((p, y) => !neg ? p*y : p/y, 1n);
    } catch (e) {
        return Infinity;
    }
};
