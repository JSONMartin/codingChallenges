/**
 * Created by jsonmartin on 5/5/16.
 */
/*
 In this kata, we want to convert a URL query string into a nested object. The query string will contain parameters that may or may not have embedded dots ('.'), and these dots will be used to break up the properties into the nested object.

 You will receive a string input that looks something like this:

 user.name.firstname=Bob&user.name.lastname=Smith&user.favoritecolor=Light%20Blue

 Your method should return an object hash-map that looks like this:

 {
   'user': {
     'name': {
     'firstname': 'Bob',
     'lastname': 'Smith'
     },
   'favoritecolor': 'Light Blue'
   }
 }
 */

'use strict';
function convertQueryToMapRefactored(query) {
  let obj = {};

  query.split('&').map(element => {
    let params = element.split('=');
    let objs = params[0].split('.');
    let assignment = params[1];

    objs.reduce( (cur, next, idx, arr) => {
      if(idx < arr.length - 1) { // Index is less than the last element to be assigned, so check if exists in OBJ
        cur[next] = cur[next] || {};
        return cur[next];
      } else { // Index is last item, so assign to OBJ the decoded string
        cur[next] = decodeURIComponent(assignment);
      }
    },obj);

  });

  return obj;
}

function convertQueryToMap(query) {
  let result = {};
  if(query === '') { return result; } // If query is blank, return an empty object
  let queryArr = query.split("&"); // Split query based on & sign
  queryArr.forEach(prop => { //Split each element by assignment
    let query = prop.split("=");
    let assignment = decodeURIComponent(query[1]); // Decode the URI encoded text back into string
    let individualProperty = query[0].split('.'); // Split each subobject by their respective periods
    let curProp = ""; // Start with a blank property
    let curObj = result; // Start with root object
    let i = 0;
    for(i; i < individualProperty.length - 1; i++) {
      curProp = individualProperty[i]; // Sets curProp to current iterated property
      if(!curObj.hasOwnProperty(curProp)) { // If the object does not exist, create it
        curObj[curProp] = {};
      }
      curObj = curObj[curProp]; // Set the object reference to the current position
    }
    curObj[individualProperty[i]] = assignment; // Once all the subobjects have been verified, assign the decoded URI text
  });
  return result;
}

/* TESTS */

var q = 'user.name.firstname=Bob&user.name.lastname=Smith&user.favoritecolor=Light%20Blue',
  out = {
    'user': {
      'name': {
        'firstname': 'Bob',
        'lastname': 'Smith'
      },
      'favoritecolor': 'Light Blue'
    }
  };

console.log( convertQueryToMap(q) ) ;
console.log( convertQueryToMapRefactored(q) ) ;