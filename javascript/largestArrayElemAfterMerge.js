/**
 * @param {number[]} nums
 * @return {number}
 */

// ~80th %ile runtime, 45 %ile memory
var maxArrayValue = function (nums) {
  if (nums.length < 2)
    return nums[0];
  return nums.reduceRight((ret, next) => next > ret ? next : next + ret, 0);
};
