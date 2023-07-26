// This works on a number of testcases but fails for, e.g.,
// [2, 3, 5, 8, 10, 14].
// A better greedy approach is to use the problem's assumption that sum[i] > 0 for all i.
var canPartitionGreedy = function(nums) {
    var sum = arr => arr.reduce((ans, n) => ans + n, 0);
    let [A, B] = [[], [...nums].sort((x, y) => x-y)];
    let D = -sum(nums);
    let N = nums.length;
    while (D !== 0 && B.length) {
        console.log(`Partition at beginning of iteration:`);
        console.log(`   A = [${A.join(", ")}]`);
        console.log(`   B = [${B.join(", ")}]`);
        console.log(`   D = ${D}`);
        let i = bisect(B, Math.floor(-D/2));
        console.log(`  Element chosen: B[${i}] = ${B[i]}`);
        D += 2*B[i];
        A.push(B[i]);
        B = [...B.slice(0, i), ...B.slice(i+1)];
        if (B.length === N) {
            console.log(`Error condition: B.length not changing`);
            break;
        }
        N = B.length;
    }
    console.log(`Done.  Final state: D = ${D}`);
    return D === 0;
};

var bisect = function(arr, val) {
    let i;
    best = Infinity;
    for (i=0; i<arr.length; ++i) {
        let x = Math.abs(arr[i] - val);
        if (x > best)
            return --i;
        best = x;
    }
    return --i;
}

var canPartition = function(nums) {
    let checked = {};
    var canPartitionK = function(nums, k, left, right, depth=0) {
        //let indent = [...Array(depth).keys()].map(n => " ").join("");
        //console.log(`${indent}canPartitionK([${nums.slice(left, right+1).join(", ")}], ${k})`);
        if (left === right)
            return k === nums[left];
        if (left > right)
            return k === 0;
        if (checked[right]?.hasOwnProperty(k)) {
            return checked[right][k];
        }
        while (right >= left && nums[right] > k) {right--;}
        let res = nums[right] && (canPartitionK(nums, k - nums[right], left, right-1, depth+1) || canPartitionK(nums, k, left, right-1, depth+1));
        //console.log(`${indent}--> ${res ? "True" : "False"}`);
        checked[right] = checked[right] ?? {};
        checked[right][k] = res;
        return res;
    }
    nums.sort((x, y) => x-y);
    let S = nums.reduce((s, n) => s+n, 0);
    if (S % 2 === 1)
        return false;
    return canPartitionK(nums, S/2, 0, nums.length-1);
}

