"use strict";
var obj = {};
var str = "a.b.c"; // ==> obj = {a: {b: {c: } } } }



function strToNestedObj(str) {
  // TODO: Error checking

  let obj = {};
  let strArr = str.split('.');

  let curRef = obj;

  for(let i = 0; i < strArr.length; i++) {
    curRef = curRef[strArr[i]] = {};
    // let curElement = strArr[i];
    // let newObj = {};
    //
    // curRef[curElement] = newObj;
    // curRef = curRef[curElement];
  }

  return obj;
}
console.log ( strToNestedObj(str) );