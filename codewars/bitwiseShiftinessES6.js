/**
 * Created by jsonmartin on 5/6/16.
 */
//Source: http://www.codewars.com/kata/523fba59cb9aaaef4f000135/train/javascript

'use strict';
Number.prototype.twos = function(n) {
  let bits = (this & (1 << n) - 1).toString(2);
  //console.log(bits);
  return bits;
};

// Number.prototype.twos = function(n) { //You may assume for this excercise that  n >= 2...
//   if(this >= 0) {   //if this number is >= 0, Add extra 0s to front of binary representation
//     let binary = this.toString(2);
//     return ("0".repeat( (n - binary.length)) + binary);
//   } else { // Number is < 0, so subtract
//     let binary = Math.abs(this).toString(2);
//     let res = (binary.length < n) ? ("1".repeat((n - binary.length)) + binary) : binary;
//     return res;
//   }
// };

//POLYFILL for pre-ES6 that doesn't have string repeat method
//This is used similar to Python's "string"*3 = "stringstringstring" functionality
if (!String.prototype.repeat) {
  String.prototype.repeat = function(count) {
    'use strict';
    if (this == null) {
      throw new TypeError('can\'t convert ' + this + ' to object');
    }
    var str = '' + this;
    count = +count;
    if (count != count) {
      count = 0;
    }
    if (count < 0) {
      throw new RangeError('repeat count must be non-negative');
    }
    if (count == Infinity) {
      throw new RangeError('repeat count must be less than infinity');
    }
    count = Math.floor(count);
    if (str.length == 0 || count == 0) {
      return '';
    }
    // Ensuring count is a 31-bit integer allows us to heavily optimize the
    // main part. But anyway, most current (August 2014) browsers can't handle
    // strings 1 << 28 chars or longer, so:
    if (str.length * count >= 1 << 28) {
      throw new RangeError('repeat count must not overflow maximum string size');
    }
    var rpt = '';
    for (;;) {
      if ((count & 1) == 1) {
        rpt += str;
      }
      count >>>= 1;
      if (count == 0) {
        break;
      }
      str += str;
    }
    // Could we try:
    // return Array(count + 1).join(this);
    return rpt;
  }
}

/*
TESTS
 */

let res2 = (-2).twos(3);// == "110";
console.log("res2", res2);
let res3 = (8).twos(5);// == "01000";
console.log("res3", res3);
let res4 = (-8).twos(5);// == "11000";
console.log("res4", res4);
let res5 = (-16).twos(5);// == "10000";
console.log("res5", res5);
let res6 = (-1).twos(10);// == "10000";
console.log("res6", res6);
