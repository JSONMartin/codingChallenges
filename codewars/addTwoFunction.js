/**
 * Created by jsonmartin on 5/16/16.
 */
//Source:http://www.codewars.com/kata/a-chain-adding-function

"use strict";

let add = (a) => { // Curried solution
  let fn = (x) => add(a+x);
  fn.valueOf = () => a;
  return fn;
};


let res = add(1)(1)(9);
console.log(res);