/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    function prefixSum(nums) {
      let psum = 0;
      return nums.map(x => psum += x);
    };

        return prefixSum(nums);
};
