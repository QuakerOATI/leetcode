/*
You are given a positive integer n.

Continuously replace n with the sum of its prime factors.

Note that if a prime factor divides n multiple times, it should be included in the sum as many times as it divides n.
Return the smallest value n will take on.
*/

/**
 * @param {number} n
 * @return {number}
 */
var smallestValue = function(n) {
    // 80.95 %ile runtime
    // 9.52 %ile memory
    var sumOfPrimeFactors = (x) => factor(x).reduce((S, [p, e]) => S + p*e, 0);
    for (let prev = n, n = sumOfPrimeFactors(n); prev !== n; prev = n, n = sumOfPrimeFactors(n));
    return n;
};

var factor = function(n) {
    let f = [];
    let primes = [];
    for (let p = 2; p*p <= n; ++p) {
        if (primes.some(q => p % q === 0))
            continue;
        primes.push(p);
        let e = 0;
        for (; n % p === 0; ++e) n /= p;
        if (e > 0)
            f.push([p, e]);
    }
    if (n > 1)
        f.push([n, 1]);
    return f;
}

var primes = function*(stopWhen) {
    var p = 2;
    for (let pow = 2; !stopWhen(p); pow *= 2) {
    }
}
