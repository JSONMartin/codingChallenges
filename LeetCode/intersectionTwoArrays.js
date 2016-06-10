/**
 * Created by jsonmartin on 6/2/16.
 */
"use strict";
var intersection = function(nums1, nums2) { //Overall time complexity: O(nums1 + nums2)
  let result = [];
  let seen = {};

  for(let i = 0; i < nums1.length; i++) { // Loop through first nums array : Time Complexity — O(n1)
    let num = nums1[i];
    if(!(num in seen)) {
      seen[num] = false;
    }
  }

  for(let i = 0; i < nums2.length; i++) { // Loop through first nums array : Time complexity — O(n2)
    let num = nums2[i];
    if((num in seen)) {
      seen[num] = true;
    }
  }

  for(let num in seen) { // Loop through seen hash : Time complexity — O(ns)
    if(seen[num]) result.push(parseInt(num));
  }

  console.log(seen);

  return result;
};

let nums1;
let nums2;

nums1 = [1, 2, 2, 1];
nums2 = [2, 2];

let res = intersection(nums1, nums2);
console.log("Result:", res);