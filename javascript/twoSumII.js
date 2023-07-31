/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */

// Too compliated; ~5 %ile runtime, 5 %ile memory.
// The simplest solution is optimal here; binary search is not necessary.
var twoSum = function(numbers, target) {
    var getRange = function(n1, l, r) {
        if (l === r)
            return [l, r];
        else if (numbers[l] === n1)
            return [l, l];
        else if (numbers[r] === n1)
            return [r, r];
        while (r - l > 1) {
            let m = Math.floor((l+r)/2);
            if (numbers[m] > n1)
                r = m;
            else
                l = m;
        }
        return [l, r];
    }
    for (let i=0; i<numbers.length; ++i) {
        for (c of getRange(target - numbers[i], 0, numbers.length - 1)) {
            console.log(`Testing at indices [i, c] = [${i}, ${c}]...`);
            if (c === i)
                continue;
            else if (numbers[c] + numbers[i] === target)
                // 1-indexed
                return [Math.min(i+1, c+1), Math.max(i+1, c+1)]
        }
    }
};
