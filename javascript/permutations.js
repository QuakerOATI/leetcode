// Accepted, but this is inefficient due to the many needless copies.
var permute = function(arr) {
    var transpose = function(arr, i, j) {
        if (i === j)
            return;
        arr[j] = arr[i] + arr[j];
        arr[i] = arr[j] - arr[i];
        arr[j] -= arr[i];
    }
    if (arr.length === 0)
        return [[]];
    var ret = [];
    for (let i=0; i<arr.length; ++i) {
        transpose(arr, i, arr.length-1);
        let last = arr.pop();
        permute(arr).forEach(x => {x.push(last); ret.push(x);});
        arr.push(last);
        transpose(arr, i, arr.length-1);
    }
    return ret;
}

// A better solution:
var permute = function(arr) {
    var ret = [];
    var helper = function(j) {
        if (j >= arr.length) {
            ret.push([...arr]);
            return;
        }
        for (let i=j; i<arr.length; ++i) {
            [arr[j], arr[i]] = [arr[i], arr[j]];
            helper(j+1);
            [arr[j], arr[i]] = [arr[i], arr[j]];
        }
    }
    helper(0);
    return ret;
}

        

