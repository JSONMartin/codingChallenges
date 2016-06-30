/**
 * Created by jsonmartin on 6/21/16.
 */
"use strict";

var permuteUnique = function(nums) {
  let result = {};
  let count = 0;

  let permutation = (current, remaining) => {
    count++;
    if(remaining.length <= 0) result[current] = current;
    else {
      for(let i = 0; i < remaining.length; i++) {
        current.push(remaining[i]);
        permutation(current.slice(), remaining.slice(0, i).concat(remaining.slice(i+1)));
        current.pop();
      }
    }
  };

  permutation([], nums);
  console.log("Count:", count);
  return Object.keys(result).map((key) => result[key]); // Maps keys to their array value
};

let res = permuteUnique([1, 1, 2, 3, 4
]);
console.log(res);