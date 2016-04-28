/**
 * Created by jsonmartin on 4/28/16.
 */
/*
 Comparing objects is not an easy task in JavaScript.
 The comparison operator only returns true if both variables point to the same object,
 that's why two objects with the same properties and values are different for JavaScript, like this:

 var a = { name: 'Joe' };
 var b = { name: 'Joe' };
 a == b;  //-> false
 */
"use strict";

function deepCompare(o1, o2) {
  if(typeof(o1) !== typeof(o2)) { return false; } // Check if o1 and o2 are of different types

  if(typeof o1 === 'object' && typeof o2 === 'object') { //Check for Object
    if(o1 && o2 && (Object.keys(o1).length !== Object.keys(o2).length)) { return false; } //If o1 and o2 are valid, Check for number of keys in both o1 and o2

    for(let key in o1) { //Iterate through every item in the object
      if(typeof o1[key] === 'object' && typeof o2[key] === 'object') { // Check if each key is Object, and if so...
        deepCompare(o1[key], o2[key]); // Call Deep compare on the new object
      }

      else if(Array.isArray(o1[key]) && Array.isArray(o2[key])) { //Check for Array (arrays only have simple values, strings/booleans/numbers)
        for(let i = 0; i < o1[key].length; i++) {
          if(o1[key][i] !== o2[key][i]) {
            return false;
          }
        }
      }

      else if(o1[key] !== o2[key]) { //Otherwise, assume primitive
        return false;
      }
    }
  } else { //Not an object
    if(o1 !== o2) { //Otherwise, assume primitive
      return false;
    }
  }

  return true;
}