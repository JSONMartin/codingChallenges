/**
 * Created by jsonmartin on 6/30/16.
 */
"use strict";
//Strategy: start from the middle, and push new rows to end and shift to back
String.prototype.repeat = function(count) {
  if (count < 1) return '';
  var result = '', pattern = this.valueOf();
  while (count > 1) {
    if (count & 1) result += pattern;
    count >>= 1, pattern += pattern;
  }
  return result + pattern;
};

function diamond(n){
  if(n % 2 === 0 || n < 0) return null; //Can't be even
  
  let diam = "";

  for(let i = 1; i <= n + 1; i+=2) {
    diam += " ".repeat((n-i)/2) + "*".repeat(i) + "\n";
  }

  for(let i = n - 2; i >= 1; i-=2) {
    diam += " ".repeat((n-i)/2) + "*".repeat(i) + "\n";
  }

  return diam;
}

console.log(diamond(7));