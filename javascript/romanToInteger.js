/**
 * @param {string} s
 * @return {number}
 */

// 99 %ile runtime 55.2 %ile memory
var romanToInt = function (s) {
  if (!s)
    return 0;
  let last;
  let ans = 0;
  for (let i = s.length - 1; i >= 0; --i) {
    let curr = romToInt[s[i]];
    if (curr < last)
      ans -= curr;
    else
      ans += curr;
    last = curr;
  }
  return ans;
};

const romToInt = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000
}
