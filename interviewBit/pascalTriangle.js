/**
 * Created by jsonmartin on 5/31/16.
 */
"use strict";


function pascalsTriangle(numRows) {

  // function sanitizeInterviewBit() {
  //   if(a[0] === "") { a.shift(); } // For the InterviewBit bad parsing platform (removes extra blank string)
  //
  //   a = a.map(function(n) {
  //     return parseInt(n);
  //   }); //Makes all strings ints, because of InterviewBit bad encoding
  // }
  // sanitizeInterviewBit();
  // var arr = [
  //   [1],
  //   [1,1]
  // ];
  var arr = [];

  function generateRow(rowN) {
    //console.log("rowN:", rowN);
    if(rowN === 1) { arr.push([1]); }
    else if(rowN === 2) { arr.push([1, 1]); }
    else {
      var curRowArr = [1];
      var lastRowArr = arr[rowN - 2];
      //console.log("lastRowArr:", lastRowArr);
      for(var i = 0; i < lastRowArr.length - 1; i++) {
        curRowArr.push(lastRowArr[i] + lastRowArr[i + 1]);
      }
      curRowArr.push(1);
      arr.push(curRowArr);
    }
    //console.log(arr);
  }

  for(var j = 1; j <= numRows; j++) {
    generateRow(j);
  }

  return arr;
}

var res;

res = pascalsTriangle(5);
console.log(res);