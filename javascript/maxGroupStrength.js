/*
You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​].

Return the maximum strength of a group the teacher can create.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxStrength = function (nums) {
  // 90.91 %ile runtime
  // 90.91 %ile memory
  if (nums.length === 0)
    return 0;
  if (nums.length === 1)
    return nums[0];
  if (nums.some(x => !x))
    return Math.max(0, maxStrength(nums.filter(x => x)));
  let negs = nums.filter(x => x < 0).length;
  let prod = nums.reduce((p, x) => p * x, 1);
  return (negs % 2 === 0) ? prod : prod / (Math.max(...nums.filter(x => x < 0)));
};
