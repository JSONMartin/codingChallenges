/**
 * Created by jsonmartin on 5/3/16.
 */
'use strict';

/*
This solution containing a hash map of already calculated values (memoized)
has a run time of O(n), because it only makes one pass through the entire array
 */
var sum_pairs=function(ints, target){
  let matches = [];
  let seen = {};

  for(let i = 0; i < ints.length; i++) {
    let curValue = ints[i]; // Sets curValue to current position in ints array
    let checkValue = target - curValue; // Sets checkValue to be the target minus the current value.

    if(seen[checkValue]) { // Checks if the target minus the current value is in the hash, if so means match has been found
      matches.push([checkValue, curValue]); // Stores a tuple containing previously seen value and current value
      break; // First match found, so break out of loop
    }

    seen[curValue] = true; // Adds the current value to the seen hash
  }

  return matches.length >= 1 ? matches[0] : undefined; // If match(es) found, then grab the first item found, otherwise return undefined.
};

var sum_pairs__brute_force=function(ints, s){ // This solution works, but time complexity is O(n^2). Too slow to pass the Kata test
  console.log("Running for:", ints);
  let matches = [];
  for(let outer = 0; outer < ints.length; outer++) {
    for(let inner = outer; inner < ints.length; inner++) {
      if( (ints[outer] + ints[inner]) === s) {
        let res = [ints[outer], ints[inner]];
        console.log("Match found!:", res);
        matches[outer + inner] = res;
      }
    }
  }
  return matches.sort()[0] || undefined;
};

/*
TESTS
 */
let l1= [1, 4, 8, 7, 3, 15];
let res1 = sum_pairs(l1, 8);
console.log(res1);