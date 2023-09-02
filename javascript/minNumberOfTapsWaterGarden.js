/*
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.
*/

/**
 * @param {number} n
 * @param {number[]} ranges
 * @return {number}
 */
var minTaps = function (n, ranges) {
  // 52.94 %ile runtime
  // 35.29 %ile memory
  ranges = ranges.map((r, i) => [Math.max(0, i - r), Math.min(n, i + r)]).sort((r1, r2) => r2[0] - r1[0]);
  let R = 0, ct = 0;
  for (; ranges.length && R < n; ++ct) {
    let r = R;
    while (ranges.length && ranges.at(-1)[0] <= R) {
      r = Math.max(r, ranges.pop()[1]);
    }
    if (r <= R) return -1;
    R = r;
  }
  return R === n ? ct : -1;
};
