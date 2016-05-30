/**
 * Created by jsonmartin on 5/29/16.
 */

"use strict";

function spiralOrder(a) {
  let arr = a.slice();
  let result = [];

  if(arr.length === 1) {
    result.push(arr.pop());
  }

  while(arr.length > 1) {
    //Take top row
    arr.shift().forEach((x) => result.push(x));

    //Top right to bottom right
    for(let i = 0; i < arr.length; i++) {
      result.push(arr[i].pop());
    }

    //Bottom right to bottom left
    //result.push(arr.pop().reverse());
    arr.pop().reverse().forEach((x) => result.push(x));

    //Bottom left to upper right
    for(let i = 0; i < arr.length; i++) {
      result.push(arr[i].shift());
    }
  }

  //console.log(arr.length);
  //console.log(arr);

  if(arr.length > 0) arr.forEach((x) => result.push(x));

  let resStr = "";

  result.forEach((x) => {
    resStr += x + " ";
  });

  return resStr;

  //return result.toString();

  //return result;
}

//let res = spiralOrder([[1,2,3],[4,5,6],[7,8,9]]);
//console.log(res);
// let res = spiralOrder([1]);
// console.log(res);
let res = spiralOrder(
[
  [1, 2],
    [3, 4],
    [5, 6]
]);
console.log(res);