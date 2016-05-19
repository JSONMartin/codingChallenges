/**
 * Created by jsonmartin on 5/19/16.
 */
"use strict";
//Refactored attempt
function tribonacci(signature, n) {
  let seq = signature.slice();
  while(seq.length < n) {
    seq.push(seq.slice(-3).reduce((prev, cur) => prev + cur));
  }
  return seq.slice(0, n);
}

//My first attempt — works, but clunky
function tribonacciOrig(signature,n){
  if(n === 0) { return []; }
  if(n < 3) { return signature.slice(0, n); }
  let seq = signature.slice();
  let calcTrib = (n) => {
    if(n <= seq.length - 1) {
      return seq[n];
    }
    else if(n > 0){
      let result = (calcTrib(n-3) + calcTrib(n-2) + calcTrib(n-1));
      if(!isNaN(result)) { seq.push(result); }
    }
  };
  calcTrib(n + 1);
  return seq;
}

//let res = tribonacci([1,1,1],10); // [1,1,1,3,5,9,17,31,57,105]
//let res = tribonacci([1,1,1],10); // [1,1,1,3]
//let res = tribonacci([0,0,1],10); //,[0,0,1,1,2,4,7,13,24,44])
//let res = tribonacci([0,1,1],10); //,[0,1,1,2,4,7,13,24,44,81]
let res = tribonacci([0,0,0],10)// ,[0,0,0,0,0,0,0,0,0,0])
console.log(res);