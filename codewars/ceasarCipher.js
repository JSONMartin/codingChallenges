/**
 * Created by jsonmartin on 4/26/16.
 */

/*
LINK: http://www.codewars.com/kata/5508249a98b3234f420000fb/
 */

"use strict";

function movingShift(s, shift) {
  let shiftedStr = "";

  for(let i = 0; i < s.length; i++) {
    let curCharCode = s.charCodeAt(i);
    let curCharType = typeOfChar(curCharCode);

    if(curCharType === "upper") {
      shiftedStr += String.fromCharCode( 65 + findOffset(curCharCode, 65) );
    }
    else if(curCharType === "lower") {
      shiftedStr += String.fromCharCode( 97 + findOffset(curCharCode, 97) );
    }
    else {
      shiftedStr += String.fromCharCode(curCharCode);
    }
    shift++;
  }

  var shiftedArr = splitMessage();

  return shiftedArr;

  // HELPER METHODS

  function splitMessage() {
    let shiftedArr = [];
    let len = Math.ceil(shiftedStr.length / 5); // Find length of first 4 messages
    let lastMessageLength = shiftedStr.length - (len * 4); // Find length of last message

    for(let j = 0; j < 4; j++) {
      shiftedArr[j] = shiftedStr.substr((j * len), len);
    }
    shiftedArr[4] = shiftedStr.substr((4 * len), ((4 * len) + lastMessageLength));
    return shiftedArr;
  }

  function findOffset(curCharCode, startingChar) {
    let offset = (curCharCode - startingChar) + shift;
    if (offset >= 26) {
      offset %= 26;
    }
    return offset;
  }
}

function demovingShift(arr, shift) {
  let shiftedStr = arr.join('');
  let resultStr = "";

  for(let i = 0; i < shiftedStr.length; i++) {
    let curCharCode = shiftedStr.charCodeAt(i);
    let curCharType = typeOfChar(curCharCode);

    if(curCharType === "upper") {
      resultStr += String.fromCharCode( 65 + findOffset(curCharCode, 65) );
    }
    else if(curCharType === "lower") {
      resultStr += String.fromCharCode( 97 + findOffset(curCharCode, 97) );
    }
    else {
      resultStr += String.fromCharCode(curCharCode);
    }
    shift++;
  }

  return resultStr;

  // HELPER METHODS

  function findOffset(curCharCode, startingChar) {
    let offset = (curCharCode - startingChar) - shift;
    while(offset < 0) {
      offset+=26;
    }
    return offset;
  }
}

// HELPER METHODS

function typeOfChar(charCode) {
  if(charCode >= 65 && charCode <= 90 ) { return "upper"; }
  else if(charCode >= 97 && charCode <= 122) { return "lower"; }
  else { return "other"; }
}

/****************************************
 *               TESTS
 ****************************************/

var u = "I should have known that you would have a perfect answer for me!!!"; // -> ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]

var res = movingShift(u, 1);
console.log (res);

res = demovingShift(res, 1);
console.log(res);