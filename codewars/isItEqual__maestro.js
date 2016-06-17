"use strict";
function isItEqual(obj_1, obj2) {
  //Hacky one-liner solution, works in most cases but not if Object has custom ordering
    //return JSON.stringify(obj_1) === JSON.stringify(obj2);

  //Proper recursive solution:
  if(typeof(obj_1) !== typeof(obj2)) { return false; } // Check if obj_1 and obj2 are of different types

  if(typeof obj_1 === 'object' && typeof obj2 === 'object') { //Check for Object
    if(obj_1 && obj2 && (Object.keys(obj_1).length !== Object.keys(obj2).length)) return false; //If obj_1 and obj2 are valid, Check for number of keys in both obj_1 and obj2

    for(let key in obj_1) { //Iterate through every item in the object
      if(Array.isArray(obj_1[key]) && Array.isArray(obj2[key])) { //Check for Array
        if(obj_1[key].length !== obj2[key].length) return false; // Checks if array are different sizes, and returns false
        for(let i = 0; i < obj_1[key].length; i++) {
          if(obj_1[key][i] !== obj2[key][i]) return false;
        }
      }

      else if(typeof obj_1[key] === 'object' && typeof obj2[key] === 'object') { // Check if each key is Object, and if so...
        if(!isItEqual(obj_1[key], obj2[key])) return false; // Call isItEqual on the new object and return false if is not equal
      }

      else if(obj_1[key] !== obj2[key]) { //Otherwise, assume primitive
        return false;
      }
    }
  } else { //Not an object, assume primitive
    if(obj_1 !== obj2) return false;
  }

  return true; // If have not returned false by this point, assume object is equal
}

/*
 * TESTS
 */

let obj1 = {a: 1, b: 2, c:[1, 2, 3], e: 5, d: {a: true, b: true, c: false}};
let obj2 = {a: 1, b: 2, c:[1, 2, 3], d: {a: true, b: true, c: false}, e: 5};
let obj3 = {a: 1, b: 2, c:[1, 2, 3], d: {a: true, b: true, c: false}, e: 6};
let res = isItEqual(obj1, obj2);
console.log(res); // => true

res = isItEqual(obj1, obj3);
console.log(res); // => false


﻿
Failed to execute 'btoa' on 'Window': The string to be encoded contains characters outside of the Latin1 range.
