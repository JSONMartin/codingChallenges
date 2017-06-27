/**
    @param {number[]} nums
    @param {number} val
    @return {number}
 */

const removeElement = function(nums, val) {
    let idx = 0;
    
    while (idx < nums.length) {
        if (nums[idx] == val) {
            nums.splice(idx, 1);
            idx = 0;
        }
        else {
            idx++;
        }
    }

    return nums
}

/////////////// TESTING ///////////////
removeElement([3, 2, 2, 3], 3)