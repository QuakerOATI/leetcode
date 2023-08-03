var swap = function(arr, i, j) {
    if (i === j)
        return;
    [arr[i], arr[j]] = [arr[j], arr[i]];
};

var partitionLeft = function(arr, l, r, p) {
    let [ml, Ml] = [p, -Infinity];
    var updateRange = function(n) {
        [ml, Ml] = [Math.min(ml, n), Math.max(Ml, n)];
    }
    console.log(`Partitioning array slice [${arr.slice(l, r+1)}] on pivot ${p}...`);
    for (; arr[r] > p; r--);
    for (; arr[l] <= p; l++) updateRange(arr[l]);
    for (let i=l; i<=r; ++i) {
        if (arr[i] <= p) {
            console.log(`Swapping ${arr[i]} at index ${i} with ${arr[l]} at index ${l}`);
            console.log(`   Incrementing l = ${l} --> ${l+1}...`);
            updateRange(arr[i]);
            swap(arr, i, l++);
            for (; arr[l] <= p; l++) updateRange(arr[l]);
        } else {
            console.log(`Swapping ${arr[i]} at index ${i} with ${arr[r]} at index ${r}`);
            console.log(`   Decrementing r = ${r} --> ${r-1}...`);
            swap(arr, i, r--);
            updateRange(arr[i]);
            for (; arr[r] > p; r--);
        }
        console.log(`State at end of iteration:\n\tl = ${l}\n\tr = ${r}\n\tarr = [${arr}]`);
    }
    return {pivot: r, min: ml, max: Ml};
}

return { swap, partitionLeft };
