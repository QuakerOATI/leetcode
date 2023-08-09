/*
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.
*/

/**
 * @param {number} n
 * @return {number}
 */
var integerReplacement = function(n) {
    // 92.54 %ile runtime
    // 31.34 %ile memory
    let vec = [];
    while (n) {
        vec.push(0);
        for (let res = n % 2; n && n % 2 === res; n >>= 1)
            ++vec[vec.length-1];
    }
    let zeros = !(vec.length % 2);
    let total = 0;
    for (let i=0; i<vec.length-1; ++i) {
        if (zeros)
            total += vec[i];
        else if (vec[i] === 1) {
            total += 2;
        } else if (vec[i+1] === 1) {
            total += vec[i] + 1;
            vec[i+1] -= 1;
            vec[i+2] += 1;
        } else {
            total += vec[i] + 2;
        }
        zeros = !zeros;
    }
    if (vec.at(-1) > 2) {
        total += vec.at(-1) + 1;
    } else if (vec.at(-1) === 2) {
        total += 2;
    }
    return total;
};
