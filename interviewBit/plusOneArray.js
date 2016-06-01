/**
 * Created by jsonmartin on 5/31/16.
 */
"use strict";
function plusOne(a) {

  function sanitizeInterviewBit() {
    if(a[0] === "") { a.shift(); } // For the InterviewBit bad parsing platform (removes extra blank string)

    a = a.map(function(n) {
      return parseInt(n);
    }); //Makes all strings ints, because of InterviewBit bad encoding
  }
  sanitizeInterviewBit();



  //Remove trailing 0s
  while(a[0] === 0 && a.length > 1) {
    a.shift();
  }

  if(a.length === 1 && a[0] === 0) { return [1]; }

  //Add one to last digit
  var digitPos = a.length - 1;
  if(a[digitPos] < 9) {
    a[digitPos]++;
  } else {
    while(a[digitPos] === 9 && digitPos > 0) {
      a[digitPos] = 0;
      digitPos--;
    }
    if(digitPos === 0 && a[digitPos] === 9) {
      a[digitPos] = 0;
      a.unshift(1);
    }
    else a[digitPos]++;
  }
  return a;
}

let res;
/*
let res = plusOne([0, 1, 2, 3]); // ==> [1, 2, 4];
console.log(res);

res = plusOne([1, 2, 9, 9]); // ==> [1, 2, 4];
console.log(res);
*/

res = plusOne([0]); // ==> [1];
console.log(res);

// res = plusOne([ 9, 9, 9, 9, 9 ]); // ==> [1,0,0,0,0,0];
// console.log(res);
