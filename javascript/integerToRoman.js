/**
 * @param {number} num
 * @return {string}
 */
// Accepted, but really inefficient
// ~8 %ile
var intToRoman = function (num) {
  if (!num)
    return "";
  let ans = [];
  while (num) {
    let next = Math.max(...Object.keys(numerals).filter(n => n <= num));
    num -= next;
    ans.push(numerals[next]);
  }
  return ans.join("");
};

const numerals = {
  1: "I",
  4: "IV",
  5: "V",
  9: "IX",
  10: "X",
  40: "XL",
  50: "L",
  90: "XC",
  100: "C",
  400: "CD",
  500: "D",
  900: "CM",
  1000: "M"
};
