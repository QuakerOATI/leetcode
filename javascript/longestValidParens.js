/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function (s) {
  let partialSums = s.split("").map(x => x === "(" ? 1 : -1)
    .reduce((diffs, next) => [...diffs, diffs.at(-1) + next], [0]);
};
