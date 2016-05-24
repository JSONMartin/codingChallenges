/**
 * Created by jsonmartin on 5/23/16.
 */
"use strict";

function processData(input) {
  function factorial(n) {
    if(n === 1) { return 1; }
    else { return n * factorial(n-1); }
  }
  console.log(factorial(parseInt(input)));
}