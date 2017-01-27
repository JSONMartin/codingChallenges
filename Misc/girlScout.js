/**
 * Created by jsonmartin on 3/29/16.
 */
// https://www.interviewcake.com/question/javascript/merge-sorted-arrays?utm_source=weekly_email
'use strict';

var myArray     = [3, 4, 6, 10, 11, 15];
var alicesArray = [1, 5, 8, 12, 14, 19];

console.log(mergeArrays(myArray, alicesArray)); // logs [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

function mergeArrays(A, B) {
  var results = [];

  while(A.length > 0 && B.length > 0) {
    if(A[0] > B[0]) {
      results.push(B.shift());
    }
    else {
      results.push(A.shift());
    }
  }

  while(A.length > 0) {
    results.push(A.shift());
  }

  while(B.length > 0) {
    results.push(B.shift());
  }

  return results;
}
