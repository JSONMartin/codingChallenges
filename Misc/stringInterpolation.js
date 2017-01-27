/**
 * Created by jsonmartin on 6/21/16.
 */
/*
 Given a String in such a format: "{1,3,{5,2},{{4}}}"
 Return a "Depth Sum" such that each value has a
 N-multiplier based on how deep it's nested in brackets.


 Examples:
 "{1,3,{5,2},{{4}}}"  -> 1+3+2(5+2)+3(4) = 30
 "{1,{2,{3}},4}" -> 1 + 2(2) + 3(3) + 4 = 18

 // {1,{2,{3}},4} => 1 + 4 (depth 1)
 // {2, {{3}} => 2 (depth 2)
 // {3} => 3 (depth (3)
 // (1+4) + 2(2) + 3(3) =
 */

// Input: always valid brackets
"use strict";

function depthSumInterview(str) {
  let stringRemaining = str.substring(1, str.length - 1); // => "{1, 3, {5, 2}, {{4}}}" => "1, 3, {5, 2}, {{4}}"
  let stringArr = stringRemaining.split(','); // => [1, 3, {5, 2}, {{4}}]
  let depthObj = {};

  let total = 0;

  for(let i = 0; i < stringArr.length; i++) { // O(n^2)
    //Check for brackets
    let numOpenBrackets = stringArr[i].match(/{/g);
    //If brackets, count amount of brackets to calculate depth
    if(numOpenBrackets > 0) {
      let current = stringArr[i].replace("{", "").replace("}", "").split(",");
      for(let i = 0; i < current.length; i++) { // O(n)
        depthObj[numOpenBrackets] = (depthObj[numOpenBrackets] || 0) + current[i];
      }
    }
    else { //Else, if no brackets
      depthObj[0] = (depthObj[0] || 0) + stringArr[i];
    }
  }

  for(let key in depthObj) { // O(d)
    total += depthObj[key] * parseInt(key + 1);
  }

  return total;
}

function depthSum(str) {
  str = str.replace(/\s/g, ""); // Replaces all whitespace characters to make it less elements to iterate over
  let depthCounter = 0;

  let total = 0;
  let curNumStr = "";

  for(let i = 0; i < str.length; i++) {
    let char = str[i];

    if(!isNaN(char)) {
      curNumStr = curNumStr.trim() + char;
    }
    else {
      if(parseInt(curNumStr) > 0) {
        total+= (parseInt(curNumStr) * depthCounter);
        curNumStr="";
      }
    }

    if(char === "{") depthCounter++;
    else if(char === "}") depthCounter--;
  }

  return total;
}

//let total = depthSum('{1, 3, {5, 2}, {{4}}}');
let total = depthSum('{1,{2,{3}},4}');
console.log(total);

// {1, 3, {115, 2}, {{4}}} // => [1, 3, {115, 2}, {{4}}] => [115, 2]
// Split by commas

// DepthObj[0]: 1 + 3 = 4
// DepthObj[1]: 5 + 2 = 7
// DepthObj[2]: 4 = 4

// [1, 3, {5, 2}, {{4}}] i = 0
// {5, 2} => numOpenBrackets = 1
// [5, 2]
// {{4}} => numOpenBrackets = 2
// [4]
