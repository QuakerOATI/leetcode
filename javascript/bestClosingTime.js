/*
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
*/

/**
 * @param {string} customers
 * @return {number}
 */
var bestClosingTime = function(customers) {
    // 47.06 %ile runtime
    // 47.06 %ile memory
    let prev = 'N', total = 0, best = 0, max = -Infinity;
    customers = 'NN' + customers;
    for (let i = 0; i < customers.length - 1; ++i) {
        switch (customers[i] + customers[i+1]) {
            case ('YY'):
            case ('NY'):
                ++total;
                break;
            default:
                --total;
                break;
        }
        best = total > max ? i : best;
        max = Math.max(max, total);
    }
    return best;
};
