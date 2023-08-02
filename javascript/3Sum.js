/**
 * @param {number[]} nums
 * @return {number[][]}
 */

// Accepted, but suboptimal
// 13 %ile runtime
var threeSum = function(nums) {
    var ret = [];
    var freqs = {};
    for (let n of nums) {
        if (!freqs.hasOwnProperty(n)) freqs[n] = 1;
        else freqs[n]++;
    }
    nums = Object.entries(freqs).map(x => [parseInt(x[0]), x[1]])
                 .sort(e => e[0]);
    //console.log(nums);
    for (let i=0; i<nums.length; ++i) {
        nums[i][1]--;
        //console.log(`i = ${i}, nums[i] = ${nums[i]}`);
        for (let j=i; j<nums.length; ++j) {
            if (nums[j][1] <= 0) continue;
            nums[j][1]--;
            //console.log(`   j = ${j}, nums[j] = ${nums[j]}`);
            let s = nums[i][0] + nums[j][0];
            //console.log(`   s = ${s}`);
            let [l, r] = [nums[j][1] ? j : j+1, nums.length-1];
            for (let m=Math.floor((l+r)/2); l < r; m=Math.floor((l+r)/2)) {
                if (nums[m][0] + s < 0)
                    l = m+1;
                else
                    r = m;
            }
            if (l === r && nums[l][0] + s === 0)
                ret.push([nums[i][0], nums[j][0], nums[l][0]]);
            nums[j][1]++;
        }
        nums[i][1]++;
    }
    return ret;
}

// TLE.  Passes the "array of zeros" test but fails on nontrivial large arrays
var threeSumCounter = function(nums) {
    var ret = [];
    var seen = new Set();
    var freqs = {};
    for (let n of nums) {
        if (!freqs.hasOwnProperty(n)) freqs[n] = 1;
        else freqs[n]++;
    }
    nums = Object.entries(freqs).map(x => [parseInt(x[0]), x[1]]);
    //console.log(nums);
    for (let i=0; i<nums.length; ++i) {
        nums[i][1]--;
        //console.log(`i = ${i}`);
        for (let j=i; j<nums.length; ++j) {
            if (nums[j][1] <= 0) continue;
            nums[j][1]--;
            //console.log(`   j = ${j}`);
            for (let k=j; k<nums.length; ++k) {
                if (nums[k][1] <= 0) continue;
                nums[k][1]--;
                //console.log(`       k = ${k}`);
                let t = [nums[i], nums[j], nums[k]].map(x => x[0]).sort((x, y) => x - y);
                //console.log(`       t = [${t}]`);
                if (t.reduce((S, n) => S + n, 0) === 0) {
                    //console.log(`           Found zero-triple, checking uniqueness`);
                    let s = t.join(",");
                    if (!seen.has(s)) {
                        seen.add(s);
                        ret.push(t);
                    }
                }
                nums[k][1]++;
            }
            nums[j][1]++;
        }
        nums[i][1]++;
    }
    return ret;
};

// TLE on large array of zeros
var threeSumBruteForce = function(nums) {
    var ret = [];
    var seen = new Set();
    for (let i=0; i<nums.length; ++i) {
        for (let j=i+1; j<nums.length; ++j) {
            for (let k=j+1; k<nums.length; ++k) {
                if (nums[i] + nums[j] + nums[k] === 0) {
                    let t = [nums[i], nums[j], nums[k]];
                    let s = t.sort().join(",");
                    if (!seen.has(s)) {
                        seen.add(s);
                        ret.push(t);
                    }
                }
            }
        }
    }
    return ret;
};
