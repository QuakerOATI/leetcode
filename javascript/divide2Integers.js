/*
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [¿231, 231 ¿ 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
*/

/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    const sign = Math.sign(dividend)*Math.sign(divisor);
    const max = 2**31 + (~sign>>1);
    while (dividend > 2**31 - 1 || dividend < -(2**31)) {
        dividend >>= 1;
        divisor >>= 1;
    }
    if (divisor === 0)
        return sign*max;
    if (Math.abs(dividend) < Math.abs(divisor))
        return 0;
    if (Math.abs(divisor) === 1)
        return sign*Math.min(max, Math.abs(dividend));
    let digits = [];
    for (let D=Math.abs(dividend); D; D = Math.abs(D>>1))
        digits.push(Math.sign(dividend)*(D & 1));
    dividend = 0;
    q = 0;
    while (digits.length) {
        while (Math.abs(dividend) < Math.abs(divisor)) {
            if (!digits.length)
                return q;
            dividend <<= 1;
            q <<= 1;
            dividend += digits.pop();
        }
        q += sign;
        dividend -= sign*divisor;
    }
    return q;
};
