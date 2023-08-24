var fourSum = function(nums, target) {
    // 12.5 %ile runtime
    // 6.73 %ile memory
    if (nums.length < 4)
        return [];
    let ans = [];
    let seen = {};
    nums.sort((x, y) => x - y);
    for (let i = 0; i < nums.length - 3; ++i) {
        if (nums.slice(i, i + 4).reduce((S, x) => S + x, 0) > target)
            return ans;
        if (nums[i] + nums.slice(-3).reduce((S, x) => S + x, 0) < target)
            continue;
        for (let j = i + 1; j < nums.length - 2; ++j) {
            let T = target - nums[i] - nums[j];
            let low = nums[j+1] + nums[j+2], high = nums.at(-1) + nums.at(-2);
            if (low > T)
                break;
            else if (high < T)
                continue;
            let l = j + 1, r = nums.length - 1;
            while (l < r) {
                let S = nums[l] + nums[r];
                if (S < T)
                    ++l;
                else if (S > T)
                    --r;
                else {
                    tuple = [i, j, l, r].map(x => nums[x]);
                    if (!seen.hasOwnProperty(tuple)) {
                        ans.push(tuple);
                        seen[tuple] = true;
                    }
                    ++l;
                }
            }
        }
    }
    return ans;
}
