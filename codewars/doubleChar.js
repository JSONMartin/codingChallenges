/**
 * Created by jsonmartin on 5/14/16.
 */
//Source: http://www.codewars.com/kata/56b1f01c247c01db92000076/train/javascript
"use strict";


//Refactored solution
const doubleChar = (str) => {
  return str.split("").map(char=>char+char).join("");
};

//Old solution
// function doubleChar(str) {
//   let retStr = "";
//   for(let ch in str) {
//     retStr+=str[ch] + str[ch];
//   }
//   return retStr;
// }
