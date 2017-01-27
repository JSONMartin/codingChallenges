/**
 * Created by jsonmartin on 6/21/16.
 */
"use strict";

var permute = function(nums) {
  let results = [];

  let permutations = (current, remaining) => {
    if(remaining.length <= 0) results.push(current.slice());
    else {
      for(let i = 0; i < remaining.length; i++) { // Loop through remaining elements
        current.push(remaining[i]); // Insert the iTH element onto the end of current
        permutations(current.slice(), remaining.slice(0, i).concat(remaining.slice(i+1))); // Recurse with inserted element removed
        current.pop(); // Remove last inserted element for next iteration
      }
    }
  };

  permutations([], nums);
  return results;
};



/**
 TESTS
 **/

let res = permute([1, 2, 3]);
console.log(res);