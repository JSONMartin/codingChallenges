/**
 * Created by jsonmartin on 6/2/16.
 */
"use strict";
var intersection = function(nums1, nums2) { //Overall time complexity: O(nums1 + nums2)
  let result = [];
  let seen1 = {};
  let seen2 = {};

  for(let i = 0; i < nums1.length; i++) { // Loop through nums1 array : Time Complexity — O(n1)
    let num = nums1[i];
    seen1[num] = seen1[num] ? seen1[num] + 1 : 1;
  }

  for(let i = 0; i < nums2.length; i++) { // Loop through nums2 array : Time complexity — O(n2)
    let num = nums2[i];
    seen2[num] = seen2[num] ? seen2[num] + 1 : 1;
  }

  for(let num in seen1) { // Loop through seen hash : Time complexity — O(ns)
    if(num in seen2) {
      let minSeenTimes = Math.min(seen1[num], seen2[num]);
      for(let i = 0; i < minSeenTimes; i++) { // Pushes amount of time seen into array
        result.push(parseInt(num));
      }
    }
  }
  return result;
};

let nums1;
let nums2;

nums1 = [1, 2, 2, 1];
nums2 = [2, 2];

let res = intersection(nums1, nums2);
console.log("Result:", res);