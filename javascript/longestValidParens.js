/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function (s) {
  let stack = [];
  let maxLength = 0;
  let adjacent = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(i);
    } else if (s[i] === ")") {
      if (stack.length) {
        maxLength = Math.max(maxLength, i - stack.pop() + 1 + adjacent);
        adjacent = maxLength;
      } else {
        adjacent = 0;
      }
    }
  }
  return maxLength;
};

var longestValidPrefix = function (s) {
  let counter = 0;
  let longestPrefix = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      counter++;
    } else if (s[i] === ")") {
      counter--;
    }
    if (counter < 0)
      break;
    if (counter === 0)
      longestPrefix = i + 1;
  }
  return longestPrefix;
}
