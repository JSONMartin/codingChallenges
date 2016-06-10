/**
 * Created by jsonmartin on 6/1/16.
 */
"use strict";
var missingNumber = function(nums) {
  "use strict";

  if(nums.length === 1 && nums[0] === 0) { return 1; }

  for(let i = 0; i < nums.length; i++) {
    let curNum = nums[i];
    let nextNum = nums[curNum];
    while(curNum !== nextNum) {
      if(0 <= curNum && curNum < nums.length) {
        nums[curNum] = curNum;
        if(0 <= nextNum && nextNum < nums.length) {
          let tmp = nums[nextNum];
          nums[nextNum] = nextNum;
          if(nextNum === tmp) break;
          nextNum = tmp;
        } else {
          break;
        }
      } else {
        break;
      }
    }
  }

  for(let i = 0; i < nums.length; i++) {
    if(nums[i] !== i) { return i; }
  }
  return nums.length;
};

//let res = missingNumber([1, 3, 0, 2]);
let res = missingNumber([1,3,0]);
console.log(res);