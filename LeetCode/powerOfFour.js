// https://leetcode.com/problems/power-of-four/?tab=Solutions

/**
 * @param {number} num
 * @return {boolean}
 */
var isPowerOfFour = function(num) {
    if (num === 1) return true;

    let i = 1;

    while (Math.pow(4, i++) < num) {}

    return Math.pow(4, i - 1) === num;
};
