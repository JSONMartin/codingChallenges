/**************
Description

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3}
Solution solution = new Solution(nums)

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle()

// Resets the array back to its original configuration [1,2,3].
solution.reset()

// Returns the random shuffling of array [1,2,3].
solution.shuffle()
**************/

/**
* @param {number[]} nums
*/
var Solution = function(nums) {
    this.nums = nums
}

/**
* Resets the array to its original configuration and return it.
* @return {number[]}
*/
Solution.prototype.reset = function() {
    return this.nums
}

/**
* Returns a random shuffling of the array.
* @return {number[]}
*/
Solution.prototype.shuffle = function() {
    let result = [], resultSize = 0, maxSize = this.nums.length
    let indexes = {}
    let randIdx = Math.floor(Math.random() * maxSize)

    while (resultSize < maxSize) {
        while (indexes[randIdx]) {
            randIdx = Math.floor(Math.random() * maxSize)
        }
        indexes[randIdx] = true
        result.push(this.nums[randIdx])
        resultSize++
    }
    
    return result;
}

Solution.prototype.shuffleOld = function() {
    let result = []
    let nums = this.nums.slice()

    while (nums.length > 0) {
        let randIdx = Math.random()*nums.length
        result = [...result, ...nums.splice(randIdx, 1)]
    }
    
    return result;
}

var nums = [1, 2, 3]
var obj = new Solution(nums)
console.log(obj)
console.log(obj.reset())
console.log(obj.shuffle())
