/*
An array arr is a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.
*/

/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
    // 99.76 %ile runtime
    // 22.14 %ile memory
    let l = 0, r = arr.length - 1;
    while (r - l > 1) {
        let m = Math.floor((l+r)/2);
        if (arr[l] > arr[m] && arr[m] > arr[r] || arr[m] < arr[m-1])
            r = m;
        else if (arr[r] > arr[m] && arr[m] > arr[l] || arr[m] < arr[m+1])
            l = m;
        else if (arr[m] > arr[m+1] && arr[m] > arr[m-1])
            return m;
    }
    return arr[l] < arr[r] ? r : l;
};
