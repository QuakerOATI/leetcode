/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  let row = binarySearch(0, matrix.length - 1, target, (t, idx) => t - matrix[idx][0]);
  console.log(row);
  if (row < 0)
    return false;
  if (matrix[row][0] === target)
    return true;
  let j = binarySearch(0, matrix[row].length - 1, target, (t, i) => t - matrix[row][i]);
  console.log(j);
  return (0 <= j && matrix[row][j] === target);
};

var binarySearch = function (lower, upper, target, cmp) {
  while (lower < upper) {
    let m = Math.ceil((lower + upper) / 2);
    if (cmp(target, m) < 0)
      upper = m - 1;
    else
      lower = m;
  }
  return upper;
}
